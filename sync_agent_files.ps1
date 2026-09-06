param(
    [Parameter(Mandatory = $true)]
    [string]$SourceRoot,

    [Parameter(Mandatory = $true)]
    [string]$DestinationRoot
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $SourceRoot -PathType Container)) {
    throw "Source directory does not exist: $SourceRoot"
}

$excludedDirectories = @{
    '.git' = $true
    '.venv' = $true
    '.uv-cache' = $true
    '.uv-python' = $true
    '__pycache__' = $true
    '.codex_tmp' = $true
    '.agents' = $true
    '.vscode' = $true
    'output' = $true
    'outputs' = $true
    'tmp' = $true
    'tools' = $true
}

$secretPatterns = @(
    '(?i)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    '(?i)\b(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,})\b',
    '(?i)(?:api[_-]?key|client[_-]?secret|access[_-]?token|password)\s*[:=]\s*["''][^"''\r\n]{8,}["'']'
)

$eligibleExtensions = @('.md', '.py', '.pdf')
$textExtensions = @('.md', '.py')

function Get-Sha256 {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    $stream = [System.IO.File]::OpenRead($Path)
    try {
        $sha256 = [System.Security.Cryptography.SHA256]::Create()
        try {
            return ([System.BitConverter]::ToString($sha256.ComputeHash($stream))).Replace('-', '')
        }
        finally {
            $sha256.Dispose()
        }
    }
    finally {
        $stream.Dispose()
    }
}

$pendingDirectories = New-Object 'System.Collections.Generic.Stack[System.IO.DirectoryInfo]'
$candidateFiles = New-Object 'System.Collections.Generic.List[System.IO.FileInfo]'
$pendingDirectories.Push((Get-Item -LiteralPath $SourceRoot))

while ($pendingDirectories.Count -gt 0) {
    $directory = $pendingDirectories.Pop()

    foreach ($childDirectory in Get-ChildItem -LiteralPath $directory.FullName -Directory -Force) {
        if (-not $excludedDirectories.ContainsKey($childDirectory.Name)) {
            $pendingDirectories.Push($childDirectory)
        }
    }

    foreach ($file in Get-ChildItem -LiteralPath $directory.FullName -File -Force) {
        if ($eligibleExtensions -contains $file.Extension.ToLowerInvariant()) {
            $candidateFiles.Add($file)
        }
    }
}

$sourcePrefix = $SourceRoot.TrimEnd('\') + '\'
$orderedFiles = @($candidateFiles | Sort-Object FullName)

foreach ($file in $orderedFiles) {
    if ($textExtensions -notcontains $file.Extension.ToLowerInvariant()) {
        continue
    }

    $relativePath = $file.FullName.Substring($sourcePrefix.Length)
    $lineNumber = 0

    foreach ($line in [System.IO.File]::ReadLines($file.FullName)) {
        $lineNumber++
        foreach ($pattern in $secretPatterns) {
            if ($line -match $pattern) {
                throw "Potential secret found at ${relativePath}:$lineNumber. Content was not copied."
            }
        }
    }
}

$copiedCount = 0
foreach ($file in $orderedFiles) {
    $relativePath = $file.FullName.Substring($sourcePrefix.Length)
    $destinationPath = Join-Path $DestinationRoot $relativePath
    $copyRequired = -not (Test-Path -LiteralPath $destinationPath -PathType Leaf)

    if (-not $copyRequired) {
        $sourceHash = Get-Sha256 -Path $file.FullName
        $destinationHash = Get-Sha256 -Path $destinationPath
        $copyRequired = $sourceHash -ne $destinationHash
    }

    if ($copyRequired) {
        $destinationDirectory = Split-Path -Parent $destinationPath
        if (-not (Test-Path -LiteralPath $destinationDirectory -PathType Container)) {
            New-Item -ItemType Directory -Path $destinationDirectory -Force | Out-Null
        }

        Copy-Item -LiteralPath $file.FullName -Destination $destinationPath -Force
        $copiedCount++
        Write-Output "Copied: $relativePath"
    }
}

Write-Output "Eligible files: $($orderedFiles.Count); copied files: $copiedCount"
