@echo off
setlocal EnableExtensions

cd /d "%~dp0"
if errorlevel 1 exit /b 10

if not exist ".git" exit /b 11
set "SYNC_LOG=%~dp0.git\auto-sync.log"

call :sync >> "%SYNC_LOG%" 2>&1
set "SYNC_EXIT=%ERRORLEVEL%"
exit /b %SYNC_EXIT%

:sync
echo.
echo ==== [%date% %time%] GitAutoSync started ====

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ERROR: The working directory is not a Git repository.
    exit /b 12
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

git add -A
if errorlevel 1 (
    echo ERROR: git add failed.
    exit /b 20
)

git diff --cached --quiet
set "DIFF_EXIT=%ERRORLEVEL%"
if "%DIFF_EXIT%"=="1" (
    git commit -m "Auto-sync: %date% %time%"
    if errorlevel 1 (
        echo ERROR: git commit failed.
        exit /b 21
    )
) else if not "%DIFF_EXIT%"=="0" (
    echo ERROR: Could not inspect staged changes.
    exit /b 22
) else (
    echo No new local changes to commit.
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
