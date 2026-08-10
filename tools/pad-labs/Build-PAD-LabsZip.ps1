<#
.SYNOPSIS
  สร้าง PAD-Labs.zip พร้อม seed assets ครบทุก Module สำหรับแจกผ่าน GitHub Releases

.EXAMPLE
  .\Build-PAD-LabsZip.ps1
  .\Build-PAD-LabsZip.ps1 -OutDir 'D:\temp\dist'
#>
[CmdletBinding()]
param(
    [string]$RepoRoot,
    [string]$OutDir,
    [string]$ZipName = 'PAD-Labs.zip',
    [switch]$SkipXlsm
)

$ErrorActionPreference = 'Stop'

$here = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if (-not $RepoRoot) {
    $RepoRoot = (Resolve-Path (Join-Path $here '..\..')).Path
}
if (-not $OutDir) {
    $OutDir = Join-Path $RepoRoot 'dist'
}

$staging = Join-Path $OutDir '_staging\PAD-Labs'
$zipPath = Join-Path $OutDir $ZipName
$installSrc = Join-Path $here 'Install-PAD-Labs.ps1'
$readmeSrc = Join-Path $here 'PAD-Labs-README.txt'
$genXlsm = Join-Path $here 'New-Lab06SalesReport.ps1'
$fixtureXlsm = Join-Path $here 'fixtures\sales-report.xlsm'

Write-Host "RepoRoot : $RepoRoot"
Write-Host "Staging  : $staging"
Write-Host "Zip      : $zipPath"

if (Test-Path -LiteralPath (Join-Path $OutDir '_staging')) {
    Remove-Item -LiteralPath (Join-Path $OutDir '_staging') -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $staging | Out-Null
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

# Ensure Lab 06 xlsm fixture
if (-not $SkipXlsm) {
    if (-not (Test-Path -LiteralPath $fixtureXlsm)) {
        Write-Host 'สร้าง fixtures/sales-report.xlsm ...'
        & $genXlsm -RepoRoot $RepoRoot -OutputPath $fixtureXlsm
    }
}

# Seed into staging via Install -FromRepo
& $installSrc -FromRepo -RepoRoot $RepoRoot -TargetRoot $staging -Force

# Package extras
Copy-Item -LiteralPath $installSrc -Destination (Join-Path $staging 'Install-PAD-Labs.ps1') -Force
if (Test-Path -LiteralPath $readmeSrc) {
    Copy-Item -LiteralPath $readmeSrc -Destination (Join-Path $staging 'README.txt') -Force
}

# Version stamp
$stamp = @"
PAD Lab Kit — working tree for C:\PAD-Labs
Built: $((Get-Date).ToString('yyyy-MM-dd HH:mm:ss'))
Repo: $RepoRoot
"@
Set-Content -LiteralPath (Join-Path $staging 'BUILD.txt') -Value $stamp -Encoding utf8

if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}

# Compress PAD-Labs folder so extract-to-C:\ yields C:\PAD-Labs\...
Push-Location (Join-Path $OutDir '_staging')
try {
    Compress-Archive -Path 'PAD-Labs' -DestinationPath $zipPath -Force
}
finally {
    Pop-Location
}

$sizeMB = [math]::Round((Get-Item $zipPath).Length / 1MB, 2)
Write-Host ''
Write-Host "OK: $zipPath ($sizeMB MB)"
Write-Host 'แจกผู้เรียน: Extract ไปที่ C:\  หรือรัน Install-PAD-Labs.ps1 ใน zip'
