@echo off
REM Double-click file nay de tu dong dong bo Notion -> glossary -> GitHub.
REM Vi tri: C:\NCKH\glossary-en-vi\update_and_push.bat
cd /d "%~dp0"
python sync_and_push.py
echo.
echo ============================================
echo  Hoan tat. Nhan phim bat ky de dong cua so.
echo ============================================
pause >nul
