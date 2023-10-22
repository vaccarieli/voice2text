@echo off
setlocal enabledelayedexpansion

set /p "input_path=Path to the file(s) you want to process: "
if "!input_path!"=="" (
    echo You did not provide a path. Exiting.
    pause
    exit /b
)

call :activate_venv
goto :launch

:launch
"%PYTHON%" app.py --path "!input_path!"
pause
exit /b

:activate_venv
set "PYTHON=%~dp0\venv\Scripts\python.exe"
echo venv !PYTHON!
exit /b
