@echo off

:: Execute the configuration
call plugin_helpers/tools/exec_config

:: Did the configuration encounter no errors?
if %errorlevel% == 0 (

    :: Call the given package
    %PYTHONEXE% %STARTDIR%\plugin_helpers\packages\%~n1.py
)
