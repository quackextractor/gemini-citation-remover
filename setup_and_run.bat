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

REM Install requirements
pip install -r requirements.txt
pip install -r requirements-dev.txt

:: Setup and run pre-commit
echo.
echo Setting up pre-commit hooks...
pre-commit install

echo Running pre-commit checks on all files...
pre-commit run --all-files

REM Run the python script
if exist "%SCRIPT_NAME%" (
    echo [3/3] Launching %SCRIPT_NAME%...
    python "%SCRIPT_NAME%"
) else (
    echo [ERROR] %SCRIPT_NAME% not found in the current directory.
    pause
)

deactivate
pause