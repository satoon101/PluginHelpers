@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Does the config file already exist?
if exist %STARTDIR%\config.ini (

    echo config.ini file already exists.  Please edit it to your liking.

) else (

    echo Creating config.ini file.  Set values to your specifications.

    :: Copy the default config
    copy plugin_helpers\windows-defaults.ini config.ini
)

echo.
echo.

:: Loop through all hooks
for %%i in (%STARTDIR%\plugin_helpers\hooks\*.*) do (

    :: Does the hook's link exist?
    if not exist %STARTDIR%\.git\hooks\%%~ni (

        :: Create the hook
        mklink /H %STARTDIR%\.git\hooks\%%~ni %%i
    )
)

git pull

pause
