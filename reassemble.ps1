param(
    [string]$PartsDirectory = ".",
    [string]$OutputPath = ""
)

$ErrorActionPreference = "Stop"
$metadataPath = Join-Path $PartsDirectory "split_metadata.json"
$metadata = Get-Content -LiteralPath $metadataPath -Raw | ConvertFrom-Json
if ([string]::IsNullOrWhiteSpace($OutputPath)) { $OutputPath = $metadata.archive }
$expectedArchiveSha = $metadata.archive_sha256
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
