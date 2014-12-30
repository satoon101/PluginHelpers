@echo off

:: Create the prerequisite array
set PREREQUISITEs[0]="configobj"
set PREREQUISITEs[1]="path.py"
set PREREQUISITEs[2]="pep8"
set PREREQUISITEs[3]="pep257"
set PREREQUISITEs[4]="pyflakes"
set PREREQUISITEs[5]="pylint"


:: Allow the use of delayed expansion
setlocal EnableDelayedExpansion

:: Execute the configuration
call exec_config

:: Did the configuration encounter no errors?
if %errorlevel% == 0 (

    :: Loop through all prerequisites
    for /F "tokens=2 delims==" %%s in ('set PREREQUISITES[') do (

        :: Print a message about the prerequisite being installed
        echo Attempting to install/upgrade %%s.
        echo.

        :: Install the prerequisite
        %PYTHONEXE% -m pip install --upgrade %%s

        echo.
    )
)
pause
