#!/usr/bin/env python3
"""Lint PAD Robin (.robin) scripts for this lab kit.

Focuses on designer Errors-list failures and Lab 07 kit rules — not enum noise.

Checks:
  - Known-bad / invented action IDs (e.g. WaitForWindowToOpen)
  - Statement-head action IDs against references/action-ids.txt
  - Live UIAutomation appmask[...] in partial-ui (desktop Contoso/Notepad)
  - Unsafe statements inside ON BLOCK ERROR / action ON ERROR when Lab 07 SET-only
  - SET names that incorrectly include %

Usage:
  python .cursor/skills/pad-robin/scripts/lint-robin.py [path ...]
  python .cursor/skills/pad-robin/scripts/lint-robin.py modules/07-contoso-invoice-ops/scripts
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # repo root
SKILL_DIR = Path(__file__).resolve().parents[1]
ACTION_IDS_PATH = SKILL_DIR / "references" / "action-ids.txt"

# PAD rejects these invented / wrong-form IDs (seen in designer Errors list).
KNOWN_BAD_ACTIONS: dict[str, str] = {
    "UIAutomation.WaitForWindow.WaitForWindowToOpen": (
        "Use WAIT (UIAutomation.WaitForWindow.ToOpenByTitleClass Title: $'''...''' "
        "Class: $'''''' FocusWindow: True) FOR 30"
    ),
    "UIAutomation.WaitForWindow.WaitForWindowToClose": (
        "Use WAIT (UIAutomation.WaitForWindow.ToCloseByTitleClass ...) FOR N"
    ),
    "UIAutomation.FocusWindow.FocusWindow": (
        "Use UIAutomation.FocusWindow.FocusByTitleClass or .Focus (with Window:)"
    ),
}

ACTION_FAMILIES = (
    "UIAutomation",
    "WebAutomation",
    "Excel",
    "File",
    "Folder",
    "System",
    "Variables",
    "Display",
    "Workstation",
    "MouseAndKeyboard",
    "Exception",
    "Outlook",
    "Email",
    "Clipboard",
    "DateTime",
    "Text",
    "Pdf",
    "Scripting",
    "HTTP",
    "OCR",
)

# Statement-leading action call (not mid-line enums like File.IfFileExists.Overwrite)
STMT_ACTION_RE = re.compile(
    r"^\s*((?:" + "|".join(ACTION_FAMILIES) + r")\.[A-Za-z0-9_.]+)"
)
WAIT_ACTION_RE = re.compile(
    r"\bWAIT\s*\(\s*((?:" + "|".join(ACTION_FAMILIES) + r")\.[A-Za-z0-9_.]+)"
)
APPMASK_RE = re.compile(r"appmask\s*\[")
SET_BAD_RE = re.compile(r"^\s*SET\s+%[^%\s]+%\s+TO\b", re.IGNORECASE)
PARTIAL_UI_RE = re.compile(r"partial-ui", re.IGNORECASE)
ALLOW_DESKTOP_APPMASK_RE = re.compile(
    r"pad-lint:\s*allow-desktop-appmask", re.IGNORECASE
)
SET_ONLY_HINT_RE = re.compile(
    r"SET-only|only contain SET|Lab\s*07|ON BLOCK ERROR.*SET",
    re.IGNORECASE,
)
ON_BLOCK_START_RE = re.compile(r"^\s*ON\s+BLOCK\s+ERROR\b", re.IGNORECASE)
ON_ACTION_ERROR_RE = re.compile(r"^\s*ON\s+ERROR\b", re.IGNORECASE)
END_RE = re.compile(r"^\s*END\b", re.IGNORECASE)
UNSAFE_IN_HANDLER_RE = re.compile(
    r"\b(Variables\.IncreaseVariable|File\.WriteText|Variables\.AddRowToDataTable|"
    r"Exception\.GetLastError|Folder\.Create|Excel\.|UIAutomation\.|WebAutomation\.)",
    re.IGNORECASE,
)
UIA_STMT_RE = re.compile(r"^\s*UIAutomation\.", re.IGNORECASE)

# Real Robin exports sometimes use Family.Action.Variant not listed as full selector.
ALLOWED_SUFFIX_ALIASES = {
    "UIAutomation.Click.Click",
    "UIAutomation.PopulateTextField.PopulateTextField",
    "UIAutomation.PopulateTextField.SimulatePopulateTextField",
    "Display.ShowMessageDialog.ShowMessage",
    "Variables.CreateNewDatatable",
    "Variables.AddRowToDataTable.AppendRowToDataTable",
    "Excel.LaunchExcel.LaunchAndOpen",
    "Excel.LaunchExcel.Launch",
    "Excel.LaunchExcel.LaunchNewDocument",
    "Excel.ReadFromExcel.ReadAllCells",
    "Excel.WriteToExcel.WriteCell",
    "Excel.WriteToExcel.WriteCells",
    "Excel.CloseExcel.Close",
    "Excel.CloseExcel.CloseAndSaveAs",
    "Excel.SaveAs.SaveAs",
    "File.WriteText",
    "File.Copy",
    "File.Delete",
    "File.GetPathPart",
    "Folder.Create",
    "Folder.GetFiles",
    "System.RunApplication.RunApplication",
    "Workstation.PlaySound.PlaySystemSound",
    "Text.Trim",
    "Text.ToNumber",
    "Text.SplitText.SplitWithDelimiter",
    "Variables.IncreaseVariable",
    "WebAutomation.LaunchEdge.LaunchEdge",
    "WebAutomation.CloseWebBrowser",
    "WebAutomation.WaitForWebPageContent.WaitForWebPageToContainElement",
    "WebAutomation.PopulateTextField.PopulateTextField",
    "WebAutomation.Click.Click",
    "Excel.RunExcelMacro.RunExcelMacro",
    "File.ReadText",
    "Exception.GetLastError",
    "DateTime.GetCurrentDateTime.GetCurrentDateTime",
}


def load_action_ids() -> set[str]:
    ids: set[str] = set(ALLOWED_SUFFIX_ALIASES)
    if ACTION_IDS_PATH.exists():
        for line in ACTION_IDS_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                ids.add(line)
    return ids


def strip_comment(line: str) -> str:
    stripped = line.lstrip()
    if stripped.startswith("#"):
        return ""
    if "$'''" in line:
        return line
    if "#" in line:
        return line.split("#", 1)[0]
    return line


def is_partial_ui(text: str) -> bool:
    head = "\n".join(text.splitlines()[:40])
    return bool(PARTIAL_UI_RE.search(head))


def allows_desktop_appmask(text: str) -> bool:
    """Contoso/desktop catch-up may ship live appmask; capture names must match ui-map."""
    head = "\n".join(text.splitlines()[:40])
    return bool(ALLOW_DESKTOP_APPMASK_RE.search(head))


def wants_set_only_handlers(text: str) -> bool:
    head = "\n".join(text.splitlines()[:30])
    return bool(SET_ONLY_HINT_RE.search(head))


def action_known(token: str, known: set[str]) -> bool:
    token = token.rstrip(".,);")
    if token in known:
        return True
    parts = token.split(".")
    while len(parts) > 2:
        parts.pop()
        if ".".join(parts) in known:
            return True
    return False


def statement_actions(code: str) -> list[str]:
    found: list[str] = []
    m = STMT_ACTION_RE.match(code)
    if m:
        found.append(m.group(1).rstrip(".,);"))
    for wm in WAIT_ACTION_RE.finditer(code):
        found.append(wm.group(1).rstrip(".,);"))
    return found


def lint_file(path: Path, known: set[str]) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    issues: list[str] = []
    partial = is_partial_ui(text)
    allow_desktop_appmask = allows_desktop_appmask(text)
    set_only = wants_set_only_handlers(text)

    handler_depth = 0
    for i, raw in enumerate(lines, start=1):
        code = strip_comment(raw)

        if ON_BLOCK_START_RE.search(raw) or ON_ACTION_ERROR_RE.search(raw):
            handler_depth += 1
        elif handler_depth > 0 and END_RE.search(raw):
            handler_depth -= 1

        if not code.strip():
            continue

        if SET_BAD_RE.search(code):
            issues.append(
                f"{path}:{i}: error: SET name must not include % (use Name not %Name%)"
            )

        # Desktop Contoso: live UIAutomation appmask is intentional when
        # `# pad-lint: allow-desktop-appmask` is set (learner captures matching names).
        if (
            partial
            and not allow_desktop_appmask
            and UIA_STMT_RE.search(code)
            and APPMASK_RE.search(code)
        ):
            issues.append(
                f"{path}:{i}: error: partial-ui live UIAutomation appmask — comment with "
                "# REBIND, or add `# pad-lint: allow-desktop-appmask` when Contoso UI "
                "lines are intentional (PAD: UI element wasn't found until capture)"
            )

        for token in statement_actions(code):
            if token in KNOWN_BAD_ACTIONS:
                issues.append(
                    f"{path}:{i}: error: bad action '{token}' — {KNOWN_BAD_ACTIONS[token]}"
                )
                continue
            if not action_known(token, known):
                issues.append(
                    f"{path}:{i}: warning: unknown action id '{token}' "
                    f"(not in {ACTION_IDS_PATH.name}; verify on Learn / sibling .robin)"
                )

        if set_only and handler_depth > 0 and UNSAFE_IN_HANDLER_RE.search(code):
            if not re.search(r"^\s*SET\b", code, re.IGNORECASE):
                issues.append(
                    f"{path}:{i}: warning: non-SET inside ON ERROR/ON BLOCK ERROR — "
                    "Lab 07 kit: use SET flags only; Increase/File/AddRow outside"
                )

    return issues


def iter_robin_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        if p.is_file() and p.suffix.lower() == ".robin":
            files.append(p)
        elif p.is_dir():
            files.extend(sorted(p.rglob("*.robin")))
    return files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint PAD Robin lab scripts")
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[ROOT / "modules"],
        help="Files or directories (default: modules/)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    args = parser.parse_args(argv)

    known = load_action_ids()
    if not known:
        print(f"warning: empty action catalog at {ACTION_IDS_PATH}", file=sys.stderr)

    files = iter_robin_files(args.paths)
    if not files:
        print("No .robin files found", file=sys.stderr)
        return 2

    all_issues: list[str] = []
    for f in files:
        all_issues.extend(lint_file(f, known))

    errors = [x for x in all_issues if ": error:" in x]
    warnings = [x for x in all_issues if ": warning:" in x]

    for line in all_issues:
        print(line)

    print(
        f"\nChecked {len(files)} file(s): {len(errors)} error(s), {len(warnings)} warning(s)"
    )
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
