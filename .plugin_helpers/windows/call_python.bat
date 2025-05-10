@echo off

:: Execute the configuration
call .plugin_helpers/windows/exec_config

:: Did the configuration encounter no errors?
if %errorlevel% == 0 (

    :: Call the given package
    %PYTHON_EXECUTABLE% %STARTDIR%\.plugin_helpers\packages\%~n1.py
)
