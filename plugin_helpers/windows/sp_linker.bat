@echo off

:: Execute the configuration
call exec_config

:: Did the configuration encounter no error?
if %errorlevel% == 0 (

    :: Call the Source.Python linker
    %PYTHONEXE% %STARTDIR%\plugin_helpers\packages\sp_linker
)
pause
