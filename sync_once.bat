@echo off
setlocal EnableExtensions

cd /d "%~dp0"
if errorlevel 1 exit /b 10

if not exist ".git" exit /b 11
set "SYNC_LOG=%~dp0.git\auto-sync.log"

"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0sync_once.ps1" >> "%SYNC_LOG%" 2>&1
exit /b %ERRORLEVEL%
