<#
.SYNOPSIS
  สร้าง sales-report.xlsm สำหรับ Lab 06 (Orders / Filtered / Summary + Lab06Macros).

.DESCRIPTION
  ใช้ Excel COM บนเครื่อง Windows ที่มี Excel ติดตั้งแล้ว
  อ่านข้อมูลจาก modules/06-data-table-excel/assets/orders-input.xlsx (หรือ .csv)
  และ import VBA จาก FormatSummary.bas
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [string]$RepoRoot,

    [Parameter(Mandatory = $false)]
    [string]$OutputPath
)

$ErrorActionPreference = 'Stop'

$here = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if (-not $RepoRoot) {
    $RepoRoot = (Resolve-Path (Join-Path $here '..\..')).Path
}
if (-not $OutputPath) {
    $OutputPath = Join-Path $here 'fixtures\sales-report.xlsm'
}
$lab06 = Join-Path $RepoRoot 'modules\06-data-table-excel\assets'
$xlsxSrc = Join-Path $lab06 'orders-input.xlsx'
$csvSrc = Join-Path $lab06 'orders-input.csv'
$basSrc = Join-Path $lab06 'vba\FormatSummary.bas'

if (-not (Test-Path -LiteralPath $basSrc)) {
    throw "ไม่พบ FormatSummary.bas: $basSrc"
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $OutputPath) | Out-Null
if (Test-Path -LiteralPath $OutputPath) {
    Remove-Item -LiteralPath $OutputPath -Force
}

# Programmatic Access to VBA may be disabled — fail with clear message
$trustHint = 'Excel → File → Options → Trust Center → Trust Center Settings → Macro Settings → เปิด "Trust access to the VBA project object model"'

$excel = $null
$wb = $null
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    $excel.AskToUpdateLinks = $false

    if (Test-Path -LiteralPath $xlsxSrc) {
        $wb = $excel.Workbooks.Open($xlsxSrc)
        # Normalize sheet name to Orders
        $wb.Worksheets.Item(1).Name = 'Orders'
    }
    else {
        $wb = $excel.Workbooks.Add()
        $wb.Worksheets.Item(1).Name = 'Orders'
        if (Test-Path -LiteralPath $csvSrc) {
            $rows = Import-Csv -LiteralPath $csvSrc
            $ws = $wb.Worksheets.Item('Orders')
            $headers = $rows[0].PSObject.Properties.Name
            for ($c = 0; $c -lt $headers.Count; $c++) {
                $ws.Cells.Item(1, $c + 1).Value2 = $headers[$c]
            }
            $r = 2
            foreach ($row in $rows) {
                for ($c = 0; $c -lt $headers.Count; $c++) {
                    $ws.Cells.Item($r, $c + 1).Value2 = $row.($headers[$c])
                }
                $r++
            }
        }
    }

    $names = @($wb.Worksheets | ForEach-Object { $_.Name })
    if ($names -notcontains 'Filtered') {
        $wsF = $wb.Worksheets.Add([Type]::Missing, $wb.Worksheets.Item($wb.Worksheets.Count))
        $wsF.Name = 'Filtered'
    }
    if ($names -notcontains 'Summary') {
        $wsS = $wb.Worksheets.Add([Type]::Missing, $wb.Worksheets.Item($wb.Worksheets.Count))
        $wsS.Name = 'Summary'
    }

    # Ensure Orders is first
    $wb.Worksheets.Item('Orders').Move($wb.Worksheets.Item(1))

    # Import VBA module (requires Trust access to VBA project object model OR Import via .bas file)
    $vbProj = $wb.VBProject
    # Remove existing Lab06Macros if re-running
    try {
        $comp = $vbProj.VBComponents.Item('Lab06Macros')
        if ($null -ne $comp) {
            $vbProj.VBComponents.Remove($comp)
        }
    }
    catch {
        # module not present
    }
    $vbProj.VBComponents.Import($basSrc)

    # 52 = xlOpenXMLWorkbookMacroEnabled (.xlsm)
    $wb.SaveAs($OutputPath, 52)
    Write-Host "Wrote $OutputPath"
}
finally {
    if ($null -ne $wb) {
        $wb.Close($false)
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($wb) | Out-Null
    }
    if ($null -ne $excel) {
        $excel.Quit()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($excel) | Out-Null
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
