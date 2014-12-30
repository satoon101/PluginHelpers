@echo off

:: Execute the configuration
call plugin_helpers/tools/exec_config

:: Did the configuration encounter no errors?
if %errorlevel% == 0 (

    %PYTHONEXE% -m pip install --upgrade -r plugin_helpers/tools/requirements.txt
)
pause
