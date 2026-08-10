# Robin patterns (this lab kit)

Examples distilled from `modules/**/scripts/*.robin`. Prefer the nearest lab script when editing.

## Paths & init

```robin
SET WorkingRoot TO $'''C:\\PAD-Labs\\working\\lab04'''
SET ApprovedCount TO 0

IF (Folder.IfFolderExists.DoesNotExist Path: $'''%WorkingRoot%\\approved''') THEN
    Folder.Create FolderPath: WorkingRoot FolderName: $'''approved''' Folder=> NewFolder
END
```

## File routing loop

```robin
Folder.GetFiles Folder: $'''%WorkingRoot%\\inbox''' FileFilter: $'''*.txt''' IncludeSubfolders: False FailOnAccessDenied: True SortBy1: Folder.SortBy.NoSort SortDescending1: False SortBy2: Folder.SortBy.NoSort SortDescending2: False SortBy3: Folder.SortBy.NoSort SortDescending3: False Files=> InboxFiles

LOOP FOREACH CurrentFile IN InboxFiles
    File.GetPathPart File: CurrentFile NameWithoutExtension=> FileNameOnly
    IF Priority = $'''High''' AND Status = $'''Ready''' THEN
        File.Move Files: CurrentFile Destination: $'''%WorkingRoot%\\approved''' IfFileExists: File.IfExists.Overwrite MovedFiles=> MovedFiles
        Variables.IncreaseVariable Value: ApprovedCount IncrementValue: 1
    ELSE
        # …
    END
END
```

## Excel read → filter → write

```robin
Excel.LaunchExcel.LaunchAndOpen Path: $'''%WorkingRoot%\\sales-report.xlsm''' Visible: True ReadOnly: False LoadAddInsAndMacros: True Instance=> Excel
Excel.ReadFromExcel.ReadAllCells Instance: Excel ReadAsText: False FirstLineIsHeader: True RangeValue=> Orders
Variables.CreateNewDatatable InputTable: { ^['OrderId', 'Amount', 'Tier'] } DataTable=> Filtered

LOOP FOREACH CurrentRow IN Orders
    Text.ToNumber Text: CurrentRow['Amount'] Number=> AmountNumber
    IF CurrentRow['Region'] = $'''BKK''' OR AmountNumber >= 10000 THEN
        Variables.AddRowToDataTable.AppendRowToDataTable DataTable: Filtered RowToAdd: [CurrentRow['OrderId'], CurrentRow['Amount'], Tier]
    END
END

IF (File.IfFile.Exists File: OutputPath) THEN
    File.Delete Files: OutputPath
END
Excel.SaveAs.SaveAs Instance: Excel DocumentFormat: Excel.DocumentFormat.ExcelMacroEnabledWorkbook DocumentPath: OutputPath
Excel.CloseExcel.Close Instance: Excel
```

## Web automation (partial-ui + REBIND)

```robin
WebAutomation.LaunchEdge.LaunchEdge Url: $'''https://pad.ontoiq.tech/pad/02-controls.html''' WindowState: WebAutomation.BrowserWindowState.Normal ClearCache: False ClearCookies: False WaitForPageToLoadTimeout: 60 Timeout: 60 BrowserInstance=> Browser

# REBIND: capture in designer, then uncomment
# WebAutomation.SetDropDownListValue ... Control: appmask['Lab03 Controls']['Ddl_Option']

File.WriteText File: $'''C:\\PAD-Labs\\output\\lab03\\controls-result.csv''' TextToWrite: CsvBody AppendNewLine: True IfFileExists: File.IfFileExists.Overwrite Encoding: File.FileEncoding.UTF8
WebAutomation.CloseWebBrowser BrowserInstance: Browser
```

## Batch row errors (SET-only handler)

Pattern from Lab 07 — log/Increase **outside** the error handler:

```robin
LOOP FOREACH CurrentInvoice IN Invoices
    SET RowFailed TO False
    BLOCK
    ON BLOCK ERROR all
        SET RowFailed TO True
        SET Status TO $'''Failed'''
        SET ErrorMessage TO $'''Row processing error'''
    END
        # row work (may fail)
    END

    IF RowFailed = True THEN
        Variables.IncreaseVariable Value: FailedCount IncrementValue: 1
        File.WriteText File: LogPath TextToWrite: LogLine AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.UTF8
    END
END
```

## Action-level ON ERROR

```robin
Text.ToNumber Text: AmountText Number=> AmountNumber
 ON ERROR
    SET RowDecision TO $'''Reject'''
    SET Status TO $'''Rejected'''
 END
```

## Text / CSV output

```robin
SET LogHeader TO $'''InvoiceId,Status,Priority'''
File.WriteText File: LogPath TextToWrite: LogHeader AppendNewLine: True IfFileExists: File.IfFileExists.Overwrite Encoding: File.FileEncoding.UTF8
SET LogLine TO $'''%InvoiceId%,%Status%,%Priority%'''
File.WriteText File: LogPath TextToWrite: LogLine AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.UTF8
```

## Wait for window (validated IDs)

PAD rejects invented forms like `UIAutomation.WaitForWindow.WaitForWindowToOpen`. Use:

```robin
WAIT (UIAutomation.WaitForWindow.ToOpenByTitleClass Title: $'''Contoso Invoicing''' Class: $'''''' FocusWindow: True) FOR 30
UIAutomation.FocusWindow.FocusByTitleClass Title: $'''Contoso Invoicing''' Class: $''''''
UIAutomation.CloseWindow.CloseByTitleClass Title: $'''Contoso Invoicing''' Class: $''''''
```

## Contoso UI create (bundled UI Elements)

Lab 07 `.robin` appends `# [ControlRepository][PowerAutomateDesktop]` with Contoso selectors renamed to ui-map names. Paste into an **empty** flow so PAD imports UI elements. Rebuild with:

```powershell
python .cursor/skills/pad-robin/scripts/bundle-contoso-appmask.py
```

```robin
UIAutomation.Click.Click Element: appmask['Contoso Invoicing']['Btn_Invoices'] ClickType: UIAutomation.ClickType.LeftClick MousePositionRelativeToElement: UIAutomation.RectangleEdgePoint.MiddleCenter OffsetX: 0 OffsetY: 0
UIAutomation.Click.Click Element: appmask['Contoso Invoicing']['Btn_NewInvoice'] ClickType: UIAutomation.ClickType.LeftClick MousePositionRelativeToElement: UIAutomation.RectangleEdgePoint.MiddleCenter OffsetX: 0 OffsetY: 0
UIAutomation.PopulateTextField.PopulateTextField TextField: appmask['Contoso Invoicing']['Txt_Account'] Text: AccountTrimmed Mode: UIAutomation.PopulateTextMode.Replace ClickType: UIAutomation.PopulateMouseClickType.SingleClick
UIAutomation.SetDropDownListValueInWindow.SetDropDownListValueByName DropDownList: appmask['Contoso Invoicing']['Cmb_Status'] OptionsNames: StatusToSet UseRegularExpressions: False
UIAutomation.Click.Click Element: appmask['Contoso Invoicing']['Btn_Save'] ClickType: UIAutomation.ClickType.LeftClick MousePositionRelativeToElement: UIAutomation.RectangleEdgePoint.MiddleCenter OffsetX: 0 OffsetY: 0
```

Header includes `# pad-lint: allow-desktop-appmask`.

## Partial vs full scripts

| Kind | Meaning |
|------|---------|
| `full` | Runnable core logic without UI capture (files/Excel/conditionals) |
| `partial-ui` | Logic + `# REBIND` stubs for **desktop** UIAutomation. Live Contoso `appmask` lines are lint errors until commented. Web Lab Hub appmask may stay live. |

Recorded UI-heavy scripts (e.g. Calculator) can be very large — edit surgically; do not reformat entire files.

## Lint

```powershell
python .cursor/skills/pad-robin/scripts/lint-robin.py modules/07-contoso-invoice-ops/scripts
```

See `scripts/lint-robin.py` and `references/action-ids.txt`.
