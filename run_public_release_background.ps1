param(
    [Parameter(Mandatory = $true)][string]$Gh,
    [Parameter(Mandatory = $true)][string]$Repository,
    [Parameter(Mandatory = $true)][string]$RepositoryDirectory,
    [Parameter(Mandatory = $true)][string]$Archive,
    [Parameter(Mandatory = $true)][string]$ArchiveHash,
    [Parameter(Mandatory = $true)][string]$Manifest,
    [Parameter(Mandatory = $true)][string]$TemporaryDirectory,
    [Parameter(Mandatory = $true)][string]$StatusFile,
    [Parameter(Mandatory = $true)][string]$LogFile,
    [int]$InitialUploaderPid = 0,
    [int]$Workers = 2
)

$ErrorActionPreference = 'Stop'
$stateDirectory = Split-Path -Parent $StatusFile
New-Item -ItemType Directory -Force -Path $stateDirectory | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $LogFile) | Out-Null

function Write-ReleaseLog([string]$Message) {
    $line = '{0} {1}' -f ([DateTime]::UtcNow.ToString('o')), $Message
    Add-Content -LiteralPath $LogFile -Value $line -Encoding utf8
}

Write-ReleaseLog "BACKGROUND_WRAPPER_STARTED pid=$PID initial_uploader_pid=$InitialUploaderPid"

if ($InitialUploaderPid -gt 0) {
    while (Get-Process -Id $InitialUploaderPid -ErrorAction SilentlyContinue) {
        Start-Sleep -Seconds 30
    }
    Write-ReleaseLog "INITIAL_UPLOADER_EXITED pid=$InitialUploaderPid"
}

# If an interrupted Python parent left GitHub CLI children alive, let those
# requests finish before the idempotent finalizer inventories remote assets.
while ($true) {
    $active = Get-CimInstance Win32_Process | Where-Object {
        $_.Name -eq 'gh.exe' -and
        $_.CommandLine -match 'release upload data-20260919-public'
    }
    if (-not $active) { break }
    Start-Sleep -Seconds 30
}

$pythonArguments = @(
    '-3',
    (Join-Path $RepositoryDirectory 'complete_public_release.py'),
    '--gh', $Gh,
    '--repo', $Repository,
    '--repo-dir', $RepositoryDirectory,
    '--archive', $Archive,
    '--archive-hash', $ArchiveHash,
    '--manifest', $Manifest,
    '--temp-dir', $TemporaryDirectory,
    '--status-file', $StatusFile,
    '--workers', $Workers,
    '--upload-timeout-seconds', '3600',
    '--upload-pass-attempts', '24',
    '--retry-wait-seconds', '300',
    '--remove-local-archive-on-success'
)

for ($attempt = 1; $attempt -le 24; $attempt++) {
    if (Test-Path -LiteralPath $StatusFile) {
        try {
            $currentStatus = (Get-Content -Raw -LiteralPath $StatusFile | ConvertFrom-Json).status
            if ($currentStatus -eq 'COMPLETE') {
                Write-ReleaseLog 'ALREADY_COMPLETE'
                exit 0
            }
        } catch {
            Write-ReleaseLog "STATUS_READ_WARNING $($_.Exception.Message)"
        }
    }

    Write-ReleaseLog "FINALIZER_ATTEMPT attempt=$attempt"
    & py @pythonArguments *>> $LogFile
    $exitCode = $LASTEXITCODE
    if ($exitCode -eq 0) {
        Write-ReleaseLog 'BACKGROUND_WRAPPER_COMPLETE'
        exit 0
    }
    Write-ReleaseLog "FINALIZER_FAILED attempt=$attempt exit_code=$exitCode"
    if ($attempt -lt 24) { Start-Sleep -Seconds 300 }
}

Write-ReleaseLog 'BACKGROUND_WRAPPER_EXHAUSTED_RETRIES'
exit 1
