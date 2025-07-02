@echo off
:: Check for admin privileges
NET SESSION >nul 2>&1
if %errorLevel% NEQ 0 (
    echo ERROR: This script requires administrative privileges.
    echo Exiting...
    exit /b 1
)

:: Check if Python is installed
python --version >nul 2>&1
if %errorLevel% NEQ 0 (
    echo ERROR: Python is not installed or not in the system PATH.
    echo Exiting...
    exit /b 1
)

:: Install requirements from requirements.txt
echo Installing Python requirements from requirements.txt...
python -m pip install -r requirements-3.4.txt

:: Check if pip install was successful
if %errorLevel% NEQ 0 (
    echo ERROR: Failed to install Python requirements.
    echo Exiting...
    exit /b 1
)

echo Creating directories...
mkdir /p C:\TMP
echo Exiting...
exit /b 1

echo Installation completed successfully.
