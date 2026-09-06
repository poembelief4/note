$ErrorActionPreference = 'Stop'

$repositoryRoot = $PSScriptRoot
$managedFolderName = 'agent' + [char]0x5B66 + [char]0x4E60
$sourceRoot = Join-Path ([Environment]::GetFolderPath('Desktop')) $managedFolderName
$destinationRoot = Join-Path $repositoryRoot $managedFolderName
$copyHelper = Join-Path $repositoryRoot 'sync_agent_files.ps1'
$expectedOrigin = 'https://github.com/poembelief4/note.git'

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,

        [int[]]$AllowedExitCodes = @(0)
    )

    & git -C $repositoryRoot @Arguments
    $exitCode = $LASTEXITCODE
    if ($AllowedExitCodes -notcontains $exitCode) {
        throw "git $($Arguments -join ' ') failed with exit code $exitCode."
    }

    return $exitCode
}

function Test-StagedChanges {
    & git -C $repositoryRoot diff --cached --quiet
    $exitCode = $LASTEXITCODE
    if ($exitCode -eq 0) {
        return $false
    }
    if ($exitCode -eq 1) {
        return $true
    }

    throw "Could not inspect staged changes; git diff exited with $exitCode."
}

function Update-FromOrigin {
    Invoke-Git -Arguments @('fetch', 'origin', 'main') | Out-Null

    & git -C $repositoryRoot merge-base --is-ancestor origin/main HEAD
    if ($LASTEXITCODE -eq 0) {
        return
    }

    Write-Output 'Integrating remote changes with a safe rebase.'
    & git -C $repositoryRoot rebase origin/main
    if ($LASTEXITCODE -ne 0) {
        & git -C $repositoryRoot rebase --abort | Out-Null
        throw 'Rebase conflict. The rebase was aborted and nothing was pushed.'
    }
}

function Push-WithOneRetry {
    & git -C $repositoryRoot push origin HEAD:main
    if ($LASTEXITCODE -eq 0) {
        return
    }

    Write-Warning 'Initial push failed; refreshing main and retrying once.'
    Update-FromOrigin
    & git -C $repositoryRoot push origin HEAD:main
    if ($LASTEXITCODE -ne 0) {
        throw 'Push failed after one safe retry.'
    }
}

function Invoke-Sync {
    Write-Output ''
    Write-Output "==== [$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] GitAutoSync started ===="

    Invoke-Git -Arguments @('rev-parse', '--is-inside-work-tree') | Out-Null
    $originUrl = (& git -C $repositoryRoot config --get remote.origin.url).Trim()
    if ($LASTEXITCODE -ne 0 -or $originUrl -ne $expectedOrigin) {
        throw "origin must be $expectedOrigin but is $originUrl."
    }

    foreach ($operationPath in @('.git\rebase-merge', '.git\rebase-apply', '.git\MERGE_HEAD')) {
        if (Test-Path -LiteralPath (Join-Path $repositoryRoot $operationPath)) {
            throw "A Git merge or rebase is already in progress: $operationPath"
        }
    }

    $mirrorStatus = @(& git -C $repositoryRoot status --porcelain -- $managedFolderName)
    if ($LASTEXITCODE -ne 0) {
        throw 'Could not inspect the managed mirror.'
    }
    if ($mirrorStatus.Count -gt 0) {
        throw 'The managed agent study mirror has local edits. Edit the source folder instead.'
    }

    Update-FromOrigin

    & $copyHelper -SourceRoot $sourceRoot -DestinationRoot $destinationRoot
    if (-not $?) {
        throw 'Agent study file validation or copy failed.'
    }

    Invoke-Git -Arguments @('add', '-A', '--', $managedFolderName) | Out-Null
    if (Test-StagedChanges) {
        Invoke-Git -Arguments @('commit', '-m', "Auto-sync agent study: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')") | Out-Null
    }
    else {
        Write-Output 'Agent study mirror is already current.'
    }

    $aheadText = (& git -C $repositoryRoot rev-list --count origin/main..HEAD).Trim()
    if ($LASTEXITCODE -ne 0) {
        throw 'Could not determine whether commits need pushing.'
    }

    $aheadCount = [int]$aheadText
    if ($aheadCount -gt 0) {
        Write-Output "Pushing $aheadCount commit(s) to origin/main."
        Push-WithOneRetry
    }
    else {
        Write-Output 'Repository is already synchronized.'
    }

    Write-Output "==== [$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] GitAutoSync completed ===="
}

try {
    Invoke-Sync
    exit 0
}
catch {
    Write-Error $_.Exception.Message
    exit 1
}
