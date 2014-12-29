@echo off

:: Execute the configuration
call exec_config

:: Did the configuration encounter no error?
if %errorlevel% == 0 (

    :: Call the plugin releaser
    setlocal
    set PYTHONPATH=%PACKAGEDIR%
    %PYTHONEXE% %STARTDIR%\plugin_helpers\packages\plugin_releaser
    endlocal
)
pause
