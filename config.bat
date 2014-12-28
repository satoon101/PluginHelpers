@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Does the config file already exist?
if not exist %STARTDIR%\config.ini (

    :: Copy the default config
    copy packages\config-defaults.ini config.ini
    pause

) else (
    echo config.ini file already exists.  Please edit it to your liking.
    pause
)
