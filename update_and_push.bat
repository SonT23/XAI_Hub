@echo off
REM Double-click file nay de tu dong dong bo Notion -> glossary -> GitHub.
REM Vi tri: C:\NCKH\glossary-en-vi\update_and_push.bat
cd /d "%~dp0"

REM Duong dan Python thuc te tren may nay (Miniconda). Neu ban cai lai Python
REM o noi khac, sua duong dan ben duoi cho dung.
set "PYTHON_EXE=C:\Users\tranq\miniconda3\python.exe"

if exist "%PYTHON_EXE%" (
    "%PYTHON_EXE%" sync_and_push.py
) else (
    echo Khong tim thay Python tai %PYTHON_EXE%
    echo Thu dung lenh "python" mac dinh trong PATH...
    python sync_and_push.py
)
echo.
echo ============================================
echo  Hoan tat. Nhan phim bat ky de dong cua so.
echo ============================================
pause >nul
