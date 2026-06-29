@echo off
cd /d "%~dp0"
git status --porcelain | findstr /R "." >nul
if %errorlevel% equ 0 (
    git add .
    git commit -m "Auto-sync: %date% %time%"
    git push origin main
)