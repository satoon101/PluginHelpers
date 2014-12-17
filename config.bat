@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Does the config file already exist?
if not exist %STARTDIR%\config.ini (

    echo Creating config.ini file.  Set values to your specifications.

    :: Create the Server directory variable
    echo.
    @echo # Set to the directory that your server's are located in.>> config.ini
    @echo SERVERSTARTDIR="C:\Servers">> config.ini
    @echo.>> config.ini

    :: Create the Release directory variable
    echo.
    @echo # Set to the directory where your releases should be placed.>> config.ini
    @echo RELEASEDIR="C:\Releases">> config.ini
    pause

) else (
    echo config.ini file already exists.  Please edit it to your liking.
    pause
)
