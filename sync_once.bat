@echo off
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul

cd /d "%~dp0"
if errorlevel 1 exit /b 10

if not exist ".git" exit /b 11
set "SYNC_LOG=%~dp0.git\auto-sync.log"

(
    call :sync
    set "SYNC_EXIT=!ERRORLEVEL!"
) >> "%SYNC_LOG%" 2>&1
exit /b %SYNC_EXIT%

:sync
echo.
echo ==== [%date% %time%] GitAutoSync started ====

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ERROR: The working directory is not a Git repository.
    exit /b 12
)

set "ORIGIN_URL="
for /f "delims=" %%R in ('git config --get remote.origin.url 2^>nul') do set "ORIGIN_URL=%%R"
if /I not "!ORIGIN_URL!"=="https://github.com/poembelief4/note.git" (
    echo ERROR: origin must use GitHub HTTPS, but is configured as !ORIGIN_URL!.
    exit /b 15
)

if exist ".git\rebase-merge" (
    echo ERROR: A rebase is already in progress. Resolve it before syncing.
    exit /b 13
)
if exist ".git\rebase-apply" (
    echo ERROR: A rebase is already in progress. Resolve it before syncing.
    exit /b 13
)
if exist ".git\MERGE_HEAD" (
    echo ERROR: A merge is already in progress. Resolve it before syncing.
    exit /b 14
)

set "MIRROR_DIRTY="
for /f "delims=" %%S in ('git status --porcelain -- "agent学习" 2^>nul') do set "MIRROR_DIRTY=1"
if defined MIRROR_DIRTY (
    echo ERROR: The managed agent学习 mirror has local edits. Edit the source folder instead.
    exit /b 16
)

git add -A -- . ":(exclude)agent学习/**"
if errorlevel 1 (
    echo ERROR: Staging non-agent notes failed.
    exit /b 20
)

git diff --cached --quiet
set "DIFF_EXIT=!ERRORLEVEL!"
if "!DIFF_EXIT!"=="1" (
    git commit -m "Auto-sync notes: %date% %time%"
    if errorlevel 1 (
        echo ERROR: Committing non-agent notes failed.
        exit /b 21
    )
) else if not "!DIFF_EXIT!"=="0" (
    echo ERROR: Could not inspect staged changes.
    exit /b 22
) else (
    echo No new non-agent note changes to commit.
)

git fetch origin main
if errorlevel 1 (
    echo ERROR: git fetch failed.
    exit /b 30
)

git merge-base --is-ancestor origin/main HEAD
if errorlevel 1 (
    echo Integrating remote changes with a safe rebase.
    git rebase origin/main
    if errorlevel 1 (
        echo ERROR: Rebase conflict. Aborting without pushing.
        git rebase --abort
        exit /b 31
    )
)

"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0sync_agent_files.ps1" -SourceRoot "%USERPROFILE%\Desktop\agent学习" -DestinationRoot "%~dp0agent学习"
if errorlevel 1 (
    echo ERROR: Agent study file validation or copy failed.
    exit /b 33
)

git add -A -- "agent学习"
if errorlevel 1 (
    echo ERROR: Staging agent study files failed.
    exit /b 34
)

git diff --cached --quiet
set "AGENT_DIFF_EXIT=!ERRORLEVEL!"
if "!AGENT_DIFF_EXIT!"=="1" (
    git commit -m "Auto-sync agent学习: %date% %time% +08:00"
    if errorlevel 1 (
        echo ERROR: Committing agent study files failed.
        exit /b 35
    )
) else if not "!AGENT_DIFF_EXIT!"=="0" (
    echo ERROR: Could not inspect staged agent study changes.
    exit /b 36
) else (
    echo Agent study mirror is already current.
)

set "AHEAD_COUNT="
for /f "delims=" %%C in ('git rev-list --count origin/main..HEAD 2^>nul') do set "AHEAD_COUNT=%%C"
if not defined AHEAD_COUNT (
    echo ERROR: Could not determine whether commits need pushing.
    exit /b 32
)

if "%AHEAD_COUNT%"=="0" (
    echo Repository is already synchronized.
    echo ==== [%date% %time%] GitAutoSync completed ====
    exit /b 0
)

echo Pushing %AHEAD_COUNT% commit(s) to origin/main.
git push origin HEAD:main
if errorlevel 1 (
    echo ERROR: git push failed.
    exit /b 40
)

echo ==== [%date% %time%] GitAutoSync completed ====
exit /b 0
