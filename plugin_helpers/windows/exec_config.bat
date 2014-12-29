@echo off

:: Store the current directory for later use
set STARTDIR=%CD%

:: Store the package directory
set PACKAGEDIR=%STARTDIR%/plugin_helpers/packages/

:: Does the config.ini file exist?
if not exist %STARTDIR%\config.ini (

    echo No config.ini file found.
    echo Please execute the setup.bat file to create the config.ini before proceeding.
    exit /b 1
)

:: Get all the configuration values
for /f "eol=# delims=" %%a in (config.ini) do (

    set "%%a"
)

:: Is PYTHONEXE defined in the config?
if not defined PYTHONEXE (

    echo Something is wrong with your config.ini file.
    echo Please delete your config.ini file and re-execute setup.bat.
    exit /b 1
)
