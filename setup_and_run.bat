@echo off
set VENV_DIR=venv
set SCRIPT_NAME=citation_remover.py

REM Check if the virtual environment exists
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo [1/3] Creating virtual environment...
    python -m venv %VENV_DIR%
) else (
    echo [1/3] Virtual environment already exists.
)

REM Activate the virtual environment
call "%VENV_DIR%\Scripts\activate.bat"

REM Check if tkinterdnd2 is installed
pip show tkinterdnd2 >nul 2>&1
if errorlevel 1 (
    echo [2/3] Installing tkinterdnd2...
    pip install tkinterdnd2
) else (
    echo [2/3] Library tkinterdnd2 is already installed.
)

REM Run the python script
if exist "%SCRIPT_NAME%" (
    echo [3/3] Launching %SCRIPT_NAME%...
    python "%SCRIPT_NAME%"
) else (
    echo [ERROR] %SCRIPT_NAME% not found in the current directory.
    pause
)

deactivate