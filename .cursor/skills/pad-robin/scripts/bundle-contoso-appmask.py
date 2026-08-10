#!/usr/bin/env python3
"""Rebuild Lab 07 Robin as paste-safe PAD script + bundled Contoso ControlRepository."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILL_DIR = Path(__file__).resolve().parents[1]
RAW = SKILL_DIR / "references" / "contoso-penbot-raw.txt"
ROBIN = ROOT / "modules" / "07-contoso-invoice-ops" / "scripts" / "07-contoso-invoice-ops.robin"
OUT_REF = SKILL_DIR / "references" / "contoso-appmask.json"

RENAME = {
    "Text 'Invoices'": "Btn_Invoices",
    "New icon": "Btn_NewInvoice",
    "Date": "Txt_Date",
    "CompanyAccount": "Txt_Account",
    "Mail": "Txt_Contact",
    "Amount": "Txt_Amount",
    "Combo Box 'ComboBox'": "Cmb_Status",
    "Image 'Image'": "Btn_Save",
}

SCRIPT = r"""# Lab07_ContosoInvoiceOps - partial-ui catch-up (PAD Robin)
# pad-lint: allow-desktop-appmask
# Bundled Contoso UI Elements in ControlRepository at end of file
# Paste into an EMPTY desktop flow (Ctrl+A in editor then Ctrl+V)
# Note: ON BLOCK ERROR / action ON ERROR may only contain SET

############################################
# SF_InitPaths
############################################
SET WorkingRoot TO $'''C:\\PAD-Labs\\working\\lab07'''
SET OutputRoot TO $'''C:\\PAD-Labs\\output\\lab07'''
SET LogPath TO $'''C:\\PAD-Labs\\logs\\lab07\\contoso-run-log.csv'''
SET ContosoPath TO $'''D:\\Program Files\\Contoso, Inc\\Contoso Invoicing\\LegacyInvoicingApp.exe'''
SET ResultsPath TO $'''C:\\PAD-Labs\\output\\lab07\\invoice-run-results.xlsx'''
SET CreatedCount TO 0
SET FailedCount TO 0
SET RejectedCount TO 0
SET SkippedCount TO 0
SET HighPriorityCount TO 0
SET Invoices TO ''
SET Results TO ''
SET RowDecision TO $''' '''
SET AccountTrimmed TO $''' '''
SET AmountNumber TO 0
SET AttachmentFiles TO ''
SET ErrorMessage TO $''' '''
SET RowFailed TO False
SET ContosoRef TO $''' '''
SET DateForContoso TO $''' '''
SET DateParts TO ''
SET StatusToSet TO $'''Open'''
SET InvoiceDate TO $''' '''
SET BriefingButton TO $''' '''
SET ScoreboardButton TO $''' '''

File.GetPathPart File: ContosoPath Directory=> ContosoWorkingDir

IF (Folder.IfFolderExists.DoesNotExist Path: $'''%OutputRoot%\\filed''') THEN
    Folder.Create FolderPath: OutputRoot FolderName: $'''filed''' Folder=> NewFolder
END

SET LogHeader TO $'''InvoiceId,Status,Priority,AttachmentFiled,ErrorMessage'''
File.WriteText File: LogPath TextToWrite: LogHeader AppendNewLine: True IfFileExists: File.IfFileExists.Overwrite Encoding: File.FileEncoding.UTF8

Excel.LaunchExcel.LaunchAndOpen Path: $'''%WorkingRoot%\\invoices-batch.xlsx''' Visible: False ReadOnly: True LoadAddInsAndMacros: False Instance=> ExcelIn
Excel.ReadFromExcel.ReadAllCells Instance: ExcelIn FirstLineIsHeader: True RangeValue=> Invoices
Excel.CloseExcel.Close Instance: ExcelIn

Variables.CreateNewDatatable InputTable: { ^['InvoiceId', 'Status', 'Priority', 'AttachmentFiled', 'ErrorMessage', 'Notes'] } DataTable=> Results

Display.ShowMessageDialog.ShowMessage Title: $'''Contoso Ops Desk''' Message: $'''Mission: clear the invoice queue. Validate, create in Contoso, file attachments, then scoreboard.''' Icon: Display.Icon.Information Buttons: Display.Buttons.OK DefaultButton: Display.DefaultButton.Button1 IsTopMost: True ButtonPressed=> BriefingButton

############################################
# SF_LaunchContoso
############################################
System.RunApplication.RunApplication ApplicationPath: ContosoPath WorkingDirectory: ContosoWorkingDir WindowStyle: System.ProcessWindowStyle.Normal ProcessId=> ContosoProcessId
WAIT (UIAutomation.WaitForWindow.ToOpenByTitleClass Title: $'''Contoso Invoicing''' Class: $'''''' FocusWindow: True) FOR 30

LOOP FOREACH CurrentInvoice IN Invoices
    SET InvoiceId TO CurrentInvoice['InvoiceId']
    SET Account TO CurrentInvoice['Account']
    SET AmountText TO CurrentInvoice['Amount']
    SET ProcessFlag TO CurrentInvoice['ProcessFlag']
    SET Contact TO CurrentInvoice['Contact']
    SET InvoiceDate TO CurrentInvoice['InvoiceDate']
    SET StatusToSet TO CurrentInvoice['StatusToSet']
    SET AttachmentFiled TO $'''No'''
    SET ErrorMessage TO $''' '''
    SET Notes TO $''' '''
    SET Priority TO $''' '''
    SET Status TO $''' '''
    SET RowDecision TO $''' '''
    SET AccountTrimmed TO $''' '''
    SET AmountNumber TO 0
    SET ContosoRef TO $''' '''
    SET DateForContoso TO InvoiceDate
    SET RowFailed TO False

    BLOCK
    ON BLOCK ERROR all
        SET RowFailed TO True
        SET Status TO $'''Failed'''
        SET ErrorMessage TO $'''Row processing error'''
    END
        ############################################
        # SF_ValidateInvoiceRow
        ############################################
        Text.Trim Text: Account TrimmedText=> AccountTrimmed
        IF IsEmpty(AccountTrimmed) THEN
            SET RowDecision TO $'''Reject'''
            SET Status TO $'''Rejected'''
            SET Notes TO $'''Gate rejected: blank Account'''
        ELSE
            Text.ToNumber Text: AmountText Number=> AmountNumber
             ON ERROR
                SET RowDecision TO $'''Reject'''
                SET Status TO $'''Rejected'''
                SET Notes TO $'''Gate rejected: Amount not numeric'''
             END
            IF RowDecision <> $'''Reject''' AND AmountNumber <= 0 THEN
                SET RowDecision TO $'''Reject'''
                SET Status TO $'''Rejected'''
                SET Notes TO $'''Gate rejected: Amount <= 0'''
            ELSE IF ProcessFlag = $'''Skip''' THEN
                SET RowDecision TO $'''Skip'''
                SET Status TO $'''Skipped'''
                SET Notes TO $'''Seeded Skip - Contoso untouched'''
            ELSE
                SET RowDecision TO $'''Create'''
            END
        END

        IF RowDecision = $'''Reject''' THEN
            Variables.IncreaseVariable Value: RejectedCount IncrementValue: 1
            Variables.AddRowToDataTable.AppendRowToDataTable DataTable: Results RowToAdd: [InvoiceId, Status, Priority, AttachmentFiled, ErrorMessage, Notes]
            SET LogLine TO $'''%InvoiceId%,%Status%,%Priority%,%AttachmentFiled%,%ErrorMessage%'''
            File.WriteText File: LogPath TextToWrite: LogLine AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.UTF8
        ELSE IF RowDecision = $'''Skip''' THEN
            Variables.IncreaseVariable Value: SkippedCount IncrementValue: 1
            Variables.AddRowToDataTable.AppendRowToDataTable DataTable: Results RowToAdd: [InvoiceId, Status, Priority, AttachmentFiled, ErrorMessage, Notes]
            SET LogLine TO $'''%InvoiceId%,%Status%,%Priority%,%AttachmentFiled%,%ErrorMessage%'''
            File.WriteText File: LogPath TextToWrite: LogLine AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.UTF8
        ELSE IF RowDecision = $'''Create''' THEN
            Text.ToNumber Text: AmountText Number=> AmountNumber
            IF AmountNumber >= 10000 THEN
                SET Priority TO $'''High'''
                SET Status TO $'''Created-HighPriority'''
                SET Notes TO $'''HIGH PRIORITY - VIP deal lane'''
                IF IsEmpty(StatusToSet) THEN
                    SET StatusToSet TO $'''Paid'''
                END
                Variables.IncreaseVariable Value: HighPriorityCount IncrementValue: 1
            ELSE
                SET Priority TO $'''Normal'''
                SET Status TO $'''Created'''
                SET Notes TO $'''Standard create'''
                IF IsEmpty(StatusToSet) THEN
                    SET StatusToSet TO $'''Open'''
                END
            END

            Text.SplitText.SplitWithDelimiter Text: InvoiceDate CustomDelimiter: $'''-''' IsRegEx: False Result=> DateParts
             ON ERROR
                SET DateForContoso TO InvoiceDate
             END
            IF DateParts.Count = 3 THEN
                SET DateForContoso TO $'''%DateParts[1]%/%DateParts[2]%/%DateParts[0]%'''
            ELSE
                SET DateForContoso TO InvoiceDate
            END

            ############################################
            # SF_CreateContosoInvoice
            ############################################
            UIAutomation.Click.Click Element: appmask['Contoso Invoicing']['Btn_Invoices'] ClickType: UIAutomation.ClickType.LeftClick MousePositionRelativeToElement: UIAutomation.RectangleEdgePoint.MiddleCenter OffsetX: 0 OffsetY: 0
            WAIT 1
            UIAutomation.Click.Click Element: appmask['Contoso Invoicing']['Btn_NewInvoice'] ClickType: UIAutomation.ClickType.LeftClick MousePositionRelativeToElement: UIAutomation.RectangleEdgePoint.MiddleCenter OffsetX: 0 OffsetY: 0
            WAIT 1
            UIAutomation.PopulateTextField.PopulateTextField TextField: appmask['Contoso Invoicing']['Txt_Date'] Text: DateForContoso Mode: UIAutomation.PopulateTextMode.Replace ClickType: UIAutomation.PopulateMouseClickType.SingleClick
            UIAutomation.PopulateTextField.PopulateTextField TextField: appmask['Contoso Invoicing']['Txt_Account'] Text: AccountTrimmed Mode: UIAutomation.PopulateTextMode.Replace ClickType: UIAutomation.PopulateMouseClickType.SingleClick
            UIAutomation.PopulateTextField.PopulateTextField TextField: appmask['Contoso Invoicing']['Txt_Contact'] Text: Contact Mode: UIAutomation.PopulateTextMode.Replace ClickType: UIAutomation.PopulateMouseClickType.SingleClick
            UIAutomation.PopulateTextField.PopulateTextField TextField: appmask['Contoso Invoicing']['Txt_Amount'] Text: AmountText Mode: UIAutomation.PopulateTextMode.Replace ClickType: UIAutomation.PopulateMouseClickType.SingleClick
            UIAutomation.SetDropDownListValueInWindow.SetDropDownListValueByName DropDownList: appmask['Contoso Invoicing']['Cmb_Status'] OptionsNames: StatusToSet UseRegularExpressions: False
            UIAutomation.Click.Click Element: appmask['Contoso Invoicing']['Btn_Save'] ClickType: UIAutomation.ClickType.LeftClick MousePositionRelativeToElement: UIAutomation.RectangleEdgePoint.MiddleCenter OffsetX: 0 OffsetY: 0
            WAIT 1

            IF Priority = $'''High''' THEN
                Workstation.PlaySound.PlaySystemSound SystemSound: System.SystemSound.Asterisk
            END

            Variables.IncreaseVariable Value: CreatedCount IncrementValue: 1

            ############################################
            # SF_FileAttachment
            ############################################
            Folder.GetFiles Folder: $'''%WorkingRoot%\\attachments''' FileFilter: $'''%InvoiceId%*''' IncludeSubfolders: False FailOnAccessDenied: True SortBy1: Folder.SortBy.NoSort SortDescending1: False SortBy2: Folder.SortBy.NoSort SortDescending2: False SortBy3: Folder.SortBy.NoSort SortDescending3: False Files=> AttachmentFiles
            IF AttachmentFiles.Count > 0 THEN
                IF (Folder.IfFolderExists.DoesNotExist Path: $'''%OutputRoot%\\filed\\%InvoiceId%''') THEN
                    Folder.Create FolderPath: $'''%OutputRoot%\\filed''' FolderName: InvoiceId Folder=> NewFolder
                END
                File.Copy Files: AttachmentFiles Destination: $'''%OutputRoot%\\filed\\%InvoiceId%''' IfFileExists: File.IfExists.Overwrite CopiedFiles=> CopiedFiles
                SET AttachmentFiled TO $'''Yes'''
                SET Notes TO $'''%Notes% | attachment filed'''
            ELSE
                SET AttachmentFiled TO $'''No'''
            END

            Variables.AddRowToDataTable.AppendRowToDataTable DataTable: Results RowToAdd: [InvoiceId, Status, Priority, AttachmentFiled, ErrorMessage, Notes]
            SET LogLine TO $'''%InvoiceId%,%Status%,%Priority%,%AttachmentFiled%,'''
            File.WriteText File: LogPath TextToWrite: LogLine AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.UTF8
        END
    END

    IF RowFailed = True THEN
        Variables.IncreaseVariable Value: FailedCount IncrementValue: 1
        Variables.AddRowToDataTable.AppendRowToDataTable DataTable: Results RowToAdd: [InvoiceId, Status, Priority, AttachmentFiled, ErrorMessage, Notes]
        SET LogLine TO $'''%InvoiceId%,Failed,%Priority%,%AttachmentFiled%,%ErrorMessage%'''
        File.WriteText File: LogPath TextToWrite: LogLine AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.UTF8
    END
END

############################################
# SF_WriteResults
############################################
IF (File.IfFile.Exists File: ResultsPath) THEN
    File.Delete Files: ResultsPath
END

Excel.LaunchExcel.Launch Visible: True Instance=> ExcelOut
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: Results Column: $'''A''' Row: 1
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: $'''Created''' Column: $'''H''' Row: 1
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: CreatedCount Column: $'''I''' Row: 1
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: $'''Rejected''' Column: $'''H''' Row: 2
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: RejectedCount Column: $'''I''' Row: 2
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: $'''Skipped''' Column: $'''H''' Row: 3
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: SkippedCount Column: $'''I''' Row: 3
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: $'''Failed''' Column: $'''H''' Row: 4
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: FailedCount Column: $'''I''' Row: 4
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: $'''HighPriority''' Column: $'''H''' Row: 5
Excel.WriteToExcel.WriteCell Instance: ExcelOut Value: HighPriorityCount Column: $'''I''' Row: 5
Excel.CloseExcel.CloseAndSaveAs Instance: ExcelOut DocumentFormat: Excel.ExcelFormat.FromExtension DocumentPath: ResultsPath

UIAutomation.CloseWindow.CloseByTitleClass Title: $'''Contoso Invoicing''' Class: $''''''

Display.ShowMessageDialog.ShowMessage Title: $'''Contoso Ops Scoreboard''' Message: $'''Created: %CreatedCount% | High Priority: %HighPriorityCount% | Rejected: %RejectedCount% | Skipped: %SkippedCount% | Failed: %FailedCount% | Results: %ResultsPath%''' Icon: Display.Icon.Information Buttons: Display.Buttons.OK DefaultButton: Display.DefaultButton.Button1 IsTopMost: True ButtonPressed=> ScoreboardButton
"""


def build_control_repo() -> str:
    raw = RAW.read_text(encoding="utf-8", errors="replace")
    match = re.search(
        r"# \[ControlRepository\]\[PowerAutomateDesktop\]\s*(\{.*\})\s*$",
        raw,
        re.S,
    )
    if not match:
        raise SystemExit("ControlRepository not found in penbot raw")

    outer = json.loads(match.group(1))
    repo = json.loads(outer["ControlRepositorySymbols"][0]["Repository"])
    screen = repo["Screens"][0]
    screen["Name"] = "Contoso Invoicing"
    for ctrl in screen["Controls"]:
        old = ctrl["Name"]
        if old not in RENAME:
            raise SystemExit(f"Unexpected control: {old}")
        ctrl["Name"] = RENAME[old]

    # Keep Repository encoding close to PAD exports (CRLF inside string).
    repo_text = json.dumps(repo, ensure_ascii=True, indent=2).replace("\n", "\r\n")
    outer["ControlRepositorySymbols"][0]["Repository"] = repo_text
    outer["ControlRepositorySymbols"][0]["IgnoreImagesOnSerialization"] = False
    outer["ControlRepositorySymbols"][0]["ImportMetadata"] = {
        "DisplayName": "Local computer",
        "ConnectionString": "",
        "Type": "Local",
        "DesktopType": "local",
    }
    outer["ControlRepositorySymbols"][0]["Name"] = "appmask"
    outer["ImageRepositorySymbol"] = {
        "Repository": '{\r\n  "Folders": [],\r\n  "Images": [],\r\n  "Version": 1\r\n}',
        "ImportMetadata": {},
        "Name": "imgrepo",
    }
    outer["ConnectionReferences"] = []

    # Match Notepad framing: marker, blank line, JSON object (no extra comments).
    pretty = json.dumps(outer, ensure_ascii=True, indent=2)
    OUT_REF.write_text(pretty + "\n", encoding="utf-8")
    return (
        "# [ControlRepository][PowerAutomateDesktop]\n"
        "\n"
        f"{pretty}\n"
    )


def main() -> None:
    if any(ord(ch) > 127 for ch in SCRIPT):
        raise SystemExit("SCRIPT contains non-ASCII; fix before write")

    # Two deliverables:
    # 1) full robin with ControlRepository (Notepad-style)
    # 2) script-only robin (always paste-safe fallback)
    repo = build_control_repo()
    full = SCRIPT.rstrip() + "\n\n" + repo
    ROBIN.write_text(full, encoding="utf-8", newline="\n")

    only = ROBIN.with_name("07-contoso-invoice-ops.script-only.robin")
    only.write_text(SCRIPT.rstrip() + "\n", encoding="utf-8", newline="\n")

    print(f"Wrote {ROBIN} ({ROBIN.stat().st_size} bytes)")
    print(f"Wrote {only} ({only.stat().st_size} bytes) paste-safe fallback")
    print("Controls:", ", ".join(RENAME.values()))


if __name__ == "__main__":
    main()
