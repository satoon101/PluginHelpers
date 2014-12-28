@echo off


:: Create the prerequisite array
set PREREQUISITEs[0]="configobj"
set PREREQUISITEs[1]="path.py"
set PREREQUISITEs[2]="pep8"
set PREREQUISITEs[3]="pep257"
set PREREQUISITEs[4]="pyflakes"
set PREREQUISITEs[5]="pylint"


:: Set the start directory for later reference
set STARTDIR="%CD%"


:: Allow the use of delayed expansion
setlocal EnableDelayedExpansion


:: Has the config.ini file been created?
if not exist %STARTDIR%\config.ini (

    :: Print a message that the user needs to create the config.ini file
    echo No config.ini file found.
    echo Please execute the config.bat file to create the config.ini before proceeding.
    pause
    exit
)


:: Get all configuration values
for /f "eol=# delims=" %%a in (config.ini) do (
    set "%%a"
)


:: Was the PYTHONEXE variable created?
if not defined PYTHONEXE (

    :: Print a message about the config issue
    echo Something is wrong with your config.ini file.
    echo Please delete your config.ini file and re-execute config.bat.
    pause
    exit
)


:: Loop through all prerequisites
for /F "tokens=2 delims==" %%s in ('set PREREQUISITES[') do (

    :: Print a message about the prerequisite being installed
    echo Attempting to install/upgrade %%s.
    echo.

    :: Install the prerequisite
    %PYTHONEXE% -m pip install --upgrade %%s

    echo.
)
pause
