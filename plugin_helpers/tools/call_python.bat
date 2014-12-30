@echo off

:: Execute the configuration
call plugin_helpers/tools/exec_config

:: Did the configuration encounter no errors?
if %errorlevel% == 0 (

    :: Call the given package
    setlocal
    set PYTHONPATH=.\plugin_helpers\packages
    %PYTHONEXE% %STARTDIR%\plugin_helpers\packages\%1
    endlocal
)
pause
