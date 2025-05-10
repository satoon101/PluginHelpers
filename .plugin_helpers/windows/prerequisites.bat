@echo off

:: Execute the configuration
call .plugin_helpers/windows/exec_config

:: Did the configuration encounter no errors?
if %errorlevel% == 0 (
    %PYTHON_EXECUTABLE% -m pip install --upgrade pip
    %PYTHON_EXECUTABLE% -m pip install --upgrade -r .plugin_helpers/tools/requirements.txt
)
pause
