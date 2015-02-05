@echo off

:: Store the current directory for later use
set STARTDIR="%CD%"

:: Does the config.ini file exist?
if not exist %STARTDIR%\config.ini (

    echo No config.ini file found.
    echo Please execute the setup.bat file to create the config.ini before proceeding.
    exit 1
)

:: Get all the configuration values
for /f "eol=# delims=" %%a in (config.ini) do (

    set "%%a"
)

:: Is PYTHON_EXECUTABLE defined in the config?
if not defined PYTHON_EXECUTABLE (

    echo Something is wrong with your config.ini file.
    echo Please delete your config.ini file and re-execute setup.bat.
    exit 1
)
