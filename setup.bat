@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Does the config file already exist?
if exist %STARTDIR%\config.ini (

    echo config.ini file already exists.  Please edit it to your liking.
    echo If there is an error in the file, please delete it and re-run this script.

) else (

    echo Creating config.ini file.  Set values to your specifications.

    :: Copy the default config
    copy plugin_helpers\windows\config.ini config.ini
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

:: Get the current git branch
for /f %%a in ('git rev-parse --abbrev-ref HEAD') do set CURRENT_BRANCH=%%a

:: Force a checkout to execute the checkout hook
git checkout %CURRENT_BRANCH%

pause
