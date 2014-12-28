@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Does the config file already exist?
if not exist %STARTDIR%\config.ini (

    echo Creating config.ini file.  Set values to your specifications.

    :: Copy the default config
    copy plugin_helpers\windows\defaults.ini config.ini
)
