Attribute VB_Name = "FormatSummary"
Option Explicit

' Import this module into the output workbook (or sales-report.xlsm template)
' then call macro name: FormatSummary
' From PAD: Run Excel Macro → Macro: FormatSummary

Public Sub FormatSummary()
    Dim ws As Worksheet
    On Error Resume Next
    Set ws = Worksheets("Filtered")
    If ws Is Nothing Then Set ws = Worksheets(1)
    On Error GoTo 0

    If ws Is Nothing Then Exit Sub

    ws.Rows(1).Font.Bold = True
    ws.Columns("A:Z").AutoFit

    With ws.Range("A1").CurrentRegion
        .Borders.LineStyle = xlContinuous
        .Borders.Weight = xlThin
    End With

    ' Highlight Gold tier rows if Tier column exists
    Dim lastRow As Long, colTier As Long, r As Long, c As Long
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    colTier = 0
    For c = 1 To ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column
        If Trim$(CStr(ws.Cells(1, c).Value)) = "Tier" Then
            colTier = c
            Exit For
        End If
    Next c

    If colTier > 0 And lastRow >= 2 Then
        For r = 2 To lastRow
            If StrComp(CStr(ws.Cells(r, colTier).Value), "Gold", vbTextCompare) = 0 Then
                ws.Rows(r).Interior.Color = RGB(255, 242, 204)
            End If
        Next r
    End If
End Sub
