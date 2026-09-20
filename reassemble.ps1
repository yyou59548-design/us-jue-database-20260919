param(
    [string]$PartsDirectory = ".",
    [string]$OutputPath = "US_JUE_DATABASE_20260919.zip"
)

$ErrorActionPreference = "Stop"
$expectedArchiveSha = "7f930eec678bcce9c62084b7d68c5e75417cbeb07b1c4cd4cd56a1e42c2447db"
$manifestPath = Join-Path $PartsDirectory "split_manifest.csv"
$parts = Import-Csv -LiteralPath $manifestPath | Sort-Object {[int]$_.part_number}

$output = [System.IO.File]::Create((Join-Path $PartsDirectory $OutputPath))
try {
    foreach ($row in $parts) {
        $partPath = Join-Path $PartsDirectory $row.part_name
        if (-not (Test-Path -LiteralPath $partPath)) { throw "Missing part: $($row.part_name)" }
        $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $partPath).Hash.ToLowerInvariant()
        if ($actual -ne $row.sha256) { throw "SHA256 mismatch: $($row.part_name)" }
        $input = [System.IO.File]::OpenRead($partPath)
        try { $input.CopyTo($output) } finally { $input.Dispose() }
    }
} finally {
    $output.Dispose()
}

$archivePath = Join-Path $PartsDirectory $OutputPath
$actualArchiveSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $archivePath).Hash.ToLowerInvariant()
if ($actualArchiveSha -ne $expectedArchiveSha) { throw "Final archive SHA256 mismatch" }
Write-Host "Verified: $archivePath"

