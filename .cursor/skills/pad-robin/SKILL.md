---
name: pad-robin
description: >-
  Author and edit Power Automate for desktop (PAD) Robin scripts for this lab kit.
  Use when writing or fixing .robin files, desktop flows, UI/web automation actions,
  Contoso/Excel/file labs, REBIND comments, ON BLOCK ERROR handlers, or Robin lint
  failures in modules/**.
paths:
  - "modules/**/*.robin"
  - "modules/**/LAB.md"
  - "modules/**/README.md"
  - "shared/**/*.md"
  - ".cursor/skills/pad-robin/**"
---

# PAD Robin (project skill)

Grounding order (highest trust first):

1. Microsoft Learn — [Actions reference](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference), [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors), [Desktop flow coding guidelines](https://learn.microsoft.com/power-automate/guidance/desktop-flow-coding-guidelines/)
2. This repo — `shared/OFFICIAL-TERMINOLOGY.md`, `shared/BEST-PRACTICES.md`, `shared/PAD-FUNDAMENTALS.md`, `shared/SELECTOR-CONVENTIONS.md`
3. Existing scripts — `modules/**/scripts/*.robin` (match nearest lab style)
4. Action catalog — `.cursor/skills/pad-robin/references/action-ids.txt` (PAD selector IDs)

Do **not** invent cloud-flow JSON or Power Fx cloud expressions. This skill is for **desktop flow / Robin** paste-into-designer scripts.

## When invoked

1. Identify the target module (`modules/<lab>/`) and read its `README.md` / `LAB.md` plus any nearby `*.robin`.
2. Prefer editing the existing `.robin` over rewriting from scratch.
3. Keep action IDs and enum forms consistent with sibling scripts (e.g. `Excel.LaunchExcel.LaunchAndOpen`, `File.IfFileExists.Overwrite`).
4. **Never invent action IDs.** Prefer IDs present in `references/action-ids.txt` or copied from a sibling `.robin` / Microsoft sample. After edits, run the Robin linter (below).
5. Mark UI that must be captured in designer with `# REBIND` — never invent fake stable `appmask[...]` selectors unless copying an existing lab pattern.
6. Point learners to paste the script into an empty PAD flow (Robin → designer rebuild).

## Lint before finish (required)

After any `.robin` change:

```powershell
python .cursor/skills/pad-robin/scripts/lint-robin.py modules/<lab>/scripts
```

Fix **error** findings before stopping. Treat **warning** seriously (unknown action IDs, non-SET inside error handlers).

Linter catches the designer Errors-list failures we have already hit in class:

| Designer error | Kit rule |
|----------------|----------|
| Module/action `WaitForWindowToOpen` wasn't found | Wrong ID — use `WAIT (UIAutomation.WaitForWindow.ToOpenByTitleClass …) FOR N` |
| UI element `… > Contoso Invoicing > Btn_…` wasn't found | `partial-ui`: keep `appmask[...]` lines **commented** until captured + renamed |
| (runtime) handler rejects Increase/File | `ON BLOCK ERROR` / action `ON ERROR`: **SET-only** in Lab 07-style loops |

## Robin conventions (this kit)

| Topic | Rule |
|-------|------|
| Paths | `C:\PAD-Labs\working\labXX`, `output\labXX`, `logs\labXX` |
| Strings | `$'''...'''` literal; paths use doubled backslash `\\` |
| Variable create | `SET Name TO value` — name **without** `%` |
| Variable use | `%Name%` inside strings/expressions |
| Data table cell | `%CurrentRow['Column']%` (brackets **inside** `%`) |
| Sections | Comment banners `# SF_<VerbNoun>` matching subflow naming |
| Header comment | `# LabXX_ShortName — full\|partial-ui` + short purpose |

### Structure template

```text
# LabXX_Name — full|partial-ui
# notes / REBIND hints

SET WorkingRoot TO $'''C:\\PAD-Labs\\working\\labXX'''
# counters / empty tables

# ensure folders (IfFolderExists → Create)
# launch / read inputs
LOOP FOREACH …
  BLOCK
  ON BLOCK ERROR all
    # prefer SET-only flags here when unsure
  END
    # work
  END
  # log / Increase / File outside handler if needed
END
# write outputs → Close Excel / CloseWebBrowser
```

### Error handling (critical)

- Designer names: **On block error**, **On error**, **Get last error** — not “try/catch”.
- In this kit, `ON BLOCK ERROR` / action `ON ERROR` often allow only **`SET`** safely (see Lab 07). Do **IncreaseVariable**, **File.WriteText**, **AddRowToDataTable** **outside** the handler after a flag like `RowFailed`.
- Lab 09 may call `Exception.GetLastError` inside handlers for teaching — when editing Lab 07-style batch loops, follow Lab 07’s SET-only constraint.
- Always plan Cleanup: Close Excel / Close web browser even on failure paths when the lab expects it.

### UI / selectors

- Web Lab Hub: prefer `#id` / `[data-pad=…]` — see `shared/SELECTOR-CONVENTIONS.md`.
- Prefer **Wait for window** / **Wait for window content** / **Wait for web page content** over blind `WAIT N` when a condition exists.
- Contoso desktop: REBIND per `modules/07-contoso-invoice-ops/assets/ui-map.md`.
- **`partial-ui` Contoso / desktop:**
  - Prefer bundling Contoso UI Elements in the `.robin` via `# [ControlRepository][PowerAutomateDesktop]` (see Lab 01b Notepad / Lab 07). Rebuild with `scripts/bundle-contoso-appmask.py` when selectors change.
  - Ship **live** `UIAutomation` + `appmask['Contoso Invoicing']['…']` named per `ui-map.md`.
  - Add header `# pad-lint: allow-desktop-appmask`.
  - If a catch-up script has **no** ControlRepository, paste will show “UI element wasn't found” until capture — avoid that for Contoso Lab 07 by bundling.
  - Title/class waits & closes may stay live without appmask.
  - Do **not** invent action forms like `UIAutomation.WaitForWindow.WaitForWindowToOpen`.
- **`partial-ui` Web Lab Hub:** `WebAutomation` + `appmask` may stay live (stable selectors).


### Validated desktop wait / focus / close (copy these)

```robin
WAIT (UIAutomation.WaitForWindow.ToOpenByTitleClass Title: $'''Contoso Invoicing''' Class: $'''''' FocusWindow: True) FOR 30
UIAutomation.FocusWindow.FocusByTitleClass Title: $'''Contoso Invoicing''' Class: $''''''
UIAutomation.CloseWindow.CloseByTitleClass Title: $'''Contoso Invoicing''' Class: $''''''
```

### Excel

- Read with `FirstLineIsHeader: True` when headers exist.
- Before fixed-path Save as: `If file exists` → `Delete` → save (overwrite policy).
- Never overwrite `assets/`; write under `C:\PAD-Labs\output\…`.
- Macros only on `.xlsm` via `Excel.RunExcelMacro`.

## Action ID quick map

Map official designer names → Robin prefixes (see `shared/OFFICIAL-TERMINOLOGY.md`):

| Designer | Robin family |
|----------|----------------|
| Set variable | `SET` / `Variables.*` |
| Launch Excel / Read / Write / Close | `Excel.*` |
| Launch new Edge / Go to / Wait / Populate / Click / Close | `WebAutomation.*` |
| Click / Populate / Wait for window / Close window | `UIAutomation.*` |
| Get files / Create folder | `Folder.*` |
| Copy / Move / Write text / Read text | `File.*` |
| For each / Loop | `LOOP FOREACH` / `LOOP WHILE` |
| If / Else if / Else | `IF` / `ELSE IF` / `ELSE` / `END` |
| On block error | `BLOCK` + `ON BLOCK ERROR` … `END` |
| Run application | `System.RunApplication.*` |
| Display message | `Display.ShowMessageDialog.ShowMessage` |
| Create new data table / Insert row | `Variables.CreateNewDatatable` / `Variables.AddRowToDataTable.*` |

When unsure of parameters, open the matching Learn page under [Actions reference](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference), check `references/action-ids.txt`, and mirror a sibling `.robin` in this repo.

## Output expectations

- Emit/edit valid Robin that pastes into PAD designer **without invented action IDs**.
- For Contoso Lab 07, ship **live** desktop `appmask` + `# pad-lint: allow-desktop-appmask` (designer missing-element errors until capture are expected).
- Preserve existing REBIND comments and lab acceptance criteria from `LAB.md`.
- Prefer minimal diffs; do not expand scope into unrelated modules.
- If Microsoft Learn and a local script disagree on enum naming, **follow the local sibling `.robin`**, then note the Learn link in a comment.
- Run `lint-robin.py` on touched scripts before finishing.

## Extra references

- [references/robin-patterns.md](references/robin-patterns.md) — copy-paste patterns from this kit
- [references/learn-links.md](references/learn-links.md) — curated Microsoft Learn URLs
- [references/action-ids.txt](references/action-ids.txt) — PAD action selector allowlist for lint
- [scripts/lint-robin.py](scripts/lint-robin.py) — Robin linter
