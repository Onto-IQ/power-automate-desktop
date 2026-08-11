<#
.SYNOPSIS
  ติดตั้ง / รีเซ็ต C:\PAD-Labs สำหรับทุก Module ของ PAD Lab Kit

.DESCRIPTION
  โหมด -FromRepo: คัดลอก assets จาก clone ของ repo
  โหมด -FromPackage: คัดลอกจากโฟลเดอร์ PAD-Labs ที่แตกจาก zip (ค่าเริ่มต้นเมื่อรันในแพ็กเกจ)

.EXAMPLE
  .\Install-PAD-Labs.ps1
  .\Install-PAD-Labs.ps1 -TargetRoot 'D:\PAD-Labs'
  .\Install-PAD-Labs.ps1 -FromRepo -RepoRoot 'D:\dev\github\Onto-IQ\power-automate-desktop'
#>
[CmdletBinding(DefaultParameterSetName = 'Package')]
param(
    [Parameter(Mandatory = $false)]
    [string]$TargetRoot = 'C:\PAD-Labs',

    [Parameter(ParameterSetName = 'Repo')]
    [switch]$FromRepo,

    [Parameter(ParameterSetName = 'Repo')]
    [string]$RepoRoot,

    [Parameter(ParameterSetName = 'Package')]
    [string]$PackageRoot = $PSScriptRoot,

    [switch]$Force
)

$ErrorActionPreference = 'Stop'

function Ensure-Dir([string]$Path) {
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
}

function Copy-Tree([string]$Src, [string]$Dst) {
    if (-not (Test-Path -LiteralPath $Src)) {
        Write-Warning "ข้าม (ไม่พบ): $Src"
        return
    }
    Ensure-Dir $Dst
    Copy-Item -Path (Join-Path $Src '*') -Destination $Dst -Recurse -Force
}

function Copy-FileToDir([string]$Src, [string]$DstDir) {
    if (-not (Test-Path -LiteralPath $Src)) {
        Write-Warning "ข้าม (ไม่พบ): $Src"
        return
    }
    Ensure-Dir $DstDir
    Copy-Item -LiteralPath $Src -Destination $DstDir -Force
}

Write-Host "=== PAD-Labs Installer ==="
Write-Host "Target: $TargetRoot"

if (Test-Path -LiteralPath $TargetRoot) {
    if (-not $Force) {
        $answer = Read-Host "พบ $TargetRoot อยู่แล้ว — ทับไฟล์ working ที่ seed ได้? (y/N)"
        if ($answer -notmatch '^(y|yes)$') {
            Write-Host 'ยกเลิก'
            exit 0
        }
    }
}

# --- folders ---
$dirs = @(
    "$TargetRoot\working",
    "$TargetRoot\output",
    "$TargetRoot\logs",
    "$TargetRoot\downloads",
    "$TargetRoot\working\lab01",
    "$TargetRoot\output\lab01",
    "$TargetRoot\working\lab01b",
    "$TargetRoot\output\lab01b",
    "$TargetRoot\working\lab02",
    "$TargetRoot\working\lab02\inbox",
    "$TargetRoot\working\lab02\archive",
    "$TargetRoot\output\lab02",
    "$TargetRoot\working\lab03",
    "$TargetRoot\output\lab03",
    "$TargetRoot\working\lab04",
    "$TargetRoot\working\lab04\inbox",
    "$TargetRoot\working\lab04\approved",
    "$TargetRoot\working\lab04\rejected",
    "$TargetRoot\working\lab04\review",
    "$TargetRoot\output\lab04",
    "$TargetRoot\working\lab05",
    "$TargetRoot\working\lab05\batch",
    "$TargetRoot\working\lab05\processed",
    "$TargetRoot\output\lab05",
    "$TargetRoot\working\lab06",
    "$TargetRoot\output\lab06",
    "$TargetRoot\working\lab07",
    "$TargetRoot\output\lab07",
    "$TargetRoot\output\lab07\filed",
    "$TargetRoot\logs\lab07",
    "$TargetRoot\working\lab08",
    "$TargetRoot\output\lab08",
    "$TargetRoot\working\lab09",
    "$TargetRoot\logs\lab09",
    "$TargetRoot\output\lab09",
    "$TargetRoot\working\lab09b",
    "$TargetRoot\logs\lab09b",
    "$TargetRoot\output\lab09b",
    "$TargetRoot\working\lab10",
    "$TargetRoot\output\lab10",
    "$TargetRoot\logs\lab10",
    "$TargetRoot\working\lab03b",
    "$TargetRoot\output\lab03b"
)
$dirs | ForEach-Object { Ensure-Dir $_ }

$here = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }

if ($FromRepo) {
    if (-not $RepoRoot) {
        $RepoRoot = (Resolve-Path (Join-Path $here '..\..')).Path
    }
    Write-Host "Source: repo $RepoRoot"

    Copy-FileToDir (Join-Path $RepoRoot 'modules\01-record-replay\assets\sample-form-input.csv') "$TargetRoot\working\lab01"
    Copy-FileToDir (Join-Path $RepoRoot 'modules\01b-notepad\assets\notepad-message.txt') "$TargetRoot\working\lab01b"

    Copy-Tree (Join-Path $RepoRoot 'modules\02-file-management\assets\inbox') "$TargetRoot\working\lab02\inbox"
    Copy-FileToDir (Join-Path $RepoRoot 'modules\03-web-scout\files\assets\upload-sample.txt') "$TargetRoot\working\lab03"
    Copy-FileToDir (Join-Path $RepoRoot 'modules\03-web-scout\ajax-table\assets\scout-criteria.csv') "$TargetRoot\working\lab03"

    Copy-Tree (Join-Path $RepoRoot 'modules\04-conditional-automation\assets\inbox') "$TargetRoot\working\lab04\inbox"
    Copy-Tree (Join-Path $RepoRoot 'modules\05-looping-files-data\assets\batch') "$TargetRoot\working\lab05\batch"

    # Lab 06
    $fixtureXlsm = Join-Path $here 'fixtures\sales-report.xlsm'
    $genScript = Join-Path $here 'New-Lab06SalesReport.ps1'
    if (Test-Path -LiteralPath $fixtureXlsm) {
        Copy-FileToDir $fixtureXlsm "$TargetRoot\working\lab06"
    }
    elseif (Test-Path -LiteralPath $genScript) {
        Write-Host 'สร้าง sales-report.xlsm ด้วย Excel COM...'
        & $genScript -RepoRoot $RepoRoot -OutputPath (Join-Path $TargetRoot 'working\lab06\sales-report.xlsm')
    }
    else {
        Copy-FileToDir (Join-Path $RepoRoot 'modules\06-data-table-excel\assets\orders-input.xlsx') "$TargetRoot\working\lab06"
        Copy-FileToDir (Join-Path $RepoRoot 'modules\06-data-table-excel\assets\vba\FormatSummary.bas') "$TargetRoot\working\lab06"
        Write-Warning 'ยังไม่มี sales-report.xlsm — สร้างตาม modules/06-data-table-excel/assets/vba/README.md'
    }
    Copy-FileToDir (Join-Path $RepoRoot 'modules\06-data-table-excel\assets\expected-summary.csv') "$TargetRoot\working\lab06"
    Copy-FileToDir (Join-Path $RepoRoot 'modules\06-data-table-excel\assets\orders-input.csv') "$TargetRoot\working\lab06"

    Copy-Tree (Join-Path $RepoRoot 'modules\07-contoso-invoice-ops\assets') "$TargetRoot\working\lab07"
    Copy-FileToDir (Join-Path $RepoRoot 'modules\08-excel-web-roundtrip\assets\leads-input.xlsx') "$TargetRoot\working\lab08"
    Copy-FileToDir (Join-Path $RepoRoot 'modules\08-excel-web-roundtrip\assets\roundtrip-proof.txt') "$TargetRoot\working\lab08"
    Copy-FileToDir (Join-Path $RepoRoot 'modules\08-excel-web-roundtrip\assets\leads-input.csv') "$TargetRoot\working\lab08"
    Copy-FileToDir (Join-Path $RepoRoot 'modules\08-excel-web-roundtrip\assets\leads-output-template.csv') "$TargetRoot\working\lab08"

    Copy-Tree (Join-Path $RepoRoot 'modules\09-error-handling\assets') "$TargetRoot\working\lab09"
    Copy-Tree (Join-Path $RepoRoot 'modules\09b-error-handling-winapp\assets') "$TargetRoot\working\lab09b"
    Copy-Tree (Join-Path $RepoRoot 'modules\10-capstone-sales-ops\assets') "$TargetRoot\working\lab10"
    Copy-Tree (Join-Path $RepoRoot 'modules\03b-public-web-alt\assets') "$TargetRoot\working\lab03b"
}
else {
    # Package mode: copy pre-seeded tree next to this script
    Write-Host "Source: package $PackageRoot"
    foreach ($name in @('working', 'output', 'logs', 'downloads')) {
        $src = Join-Path $PackageRoot $name
        if (Test-Path -LiteralPath $src) {
            Copy-Tree $src (Join-Path $TargetRoot $name)
        }
    }
}

# Placeholder keepers so empty folders survive zip
@(
    "$TargetRoot\working\lab02\archive",
    "$TargetRoot\working\lab04\approved",
    "$TargetRoot\working\lab04\rejected",
    "$TargetRoot\working\lab04\review",
    "$TargetRoot\working\lab05\processed",
    "$TargetRoot\downloads",
    "$TargetRoot\output\lab07\filed"
) | ForEach-Object {
    $keep = Join-Path $_ '.keep'
    if (-not (Test-Path -LiteralPath $keep)) {
        Set-Content -LiteralPath $keep -Value '' -Encoding ascii
    }
}

Write-Host ''
Write-Host 'โครงสร้างที่ได้:'
Get-ChildItem -LiteralPath $TargetRoot | Format-Table Name, Mode -AutoSize
Write-Host "working labs: $((Get-ChildItem "$TargetRoot\working" -Directory).Name -join ', ')"
Write-Host ''
Write-Host "เสร็จแล้ว — ใช้ path $TargetRoot ในทุก Lab"
Write-Host 'อย่าแก้ไฟล์ต้นฉบับใน modules/*/assets ของ repo'
