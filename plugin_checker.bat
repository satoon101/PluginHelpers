@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Allow the use of delayed expansion
setlocal EnableDelayedExpansion


:: A function to choose the plugin to check
:ChoosePlugin

    :: Clear the console
    cls

    echo ====================================
    echo What plugin would you like to check?
    echo ====================================
    echo.

    :: Store a base counting variable
    set /a num=0

    :: Loop through all plugins
    for /D %%i in (*.*) do (

        :: Increment the counter
        set /a num+=1

        :: Set the current option to the current branch
        set option_!num!=%%~ni
    )

    :: Loop through the options
    for /l %%a in (1, 1, %num%) do (

        ::Print the option to the console
        echo    (%%a^^^) !option_%%a!
    )

    echo.

    :: Request a choice of plugin
    set /p choice=

    :: Was the choice invalid?
    if %choice% leq 0 goto :ChoosePlugin
    if %choice% gtr %num% goto :ChoosePlugin

    :: Set the plugin value to the choice
    set PLUGIN=!option_%choice%!

    :: Set the plugin's directory
    set CHECKDIR=%STARTDIR%/%PLUGIN%/addons/source-python/plugins/%PLUGIN%

    :: If the choice is valid, check the plugin
    goto :CheckPlugin


:: A place to check a specific plugin
:CheckPlugin

    echo.

    :: Run checks
    echo.
    echo.
    echo ============================
    echo Checking for PEP8 standards:
    echo ============================
    echo.

    python -m pep8 --count --benchmark %CHECKDIR%

    echo.
    echo.
    echo ==============================
    echo Checking for PEP257 standards:
    echo ==============================
    echo.

    python -m pep257 %CHECKDIR%

    echo.
    echo.
    echo ============================
    echo Checking for unused imports:
    echo ============================
    echo.

    python -m pyflakes %CHECKDIR%

    echo.
    echo.
    echo =====================
    echo Checking with PyLint:
    echo =====================
    echo.

    python -m pylint --rcfile "%STARTDIR%"/.pylintrc %CHECKDIR% --const-rgx="(([A-Z_][A-Z0-9_]*)|([a-z_][a-z0-9_]*)|(__.*__))$" --msg-template="{msg_id}:{line:3d},{column:2d}: {msg} ({symbol})"

    goto :CheckAgain


:: A place to ask to check again
:CheckAgain
    echo.
    echo Check again?

    set /p choice=

    set result=None

    if %choice% == yes set result=True
    if %choice% == y set result=True
    if %choice% == no set result=False
    if %choice% == n set result=False

    if %result% == True goto :CheckPlugin
    if %result% == False exit
    if %result% == None goto :CheckAgain
