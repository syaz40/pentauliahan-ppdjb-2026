@echo off
setlocal enabledelayedexpansion
title GitHub Auto-Push

echo ==============================================
echo   AUTO-PUSH SCRIPT (SYNC TO GITHUB)
echo ==============================================
echo Semakan dibuat setiap 60 saat.
echo Biarkan tetingkap ini terbuka di background.
echo ==============================================

:loop
git status --porcelain > nul 2>&1
for /f "delims=" %%i in ('git status --porcelain') do set HAS_CHANGES=1

if defined HAS_CHANGES (
    echo [!time!] Perubahan dikesan! Sedang memuat naik (push)...
    git add .
    git commit -m "Auto sync dari lokal"
    git push origin main
    set HAS_CHANGES=
    echo [!time!] Selesai muat naik.
) else (
    rem echo [!time!] Tiada perubahan.
)

timeout /t 60 /nobreak > nul
goto loop
