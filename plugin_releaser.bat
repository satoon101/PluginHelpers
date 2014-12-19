@echo off


:: Set the start directory for later reference
set STARTDIR="%CD%"


:: Allow the use of delayed expansion
setlocal EnableDelayedExpansion


:: Has the config.ini file been created?
if not exist %STARTDIR%\config.ini (

    :: Print a message that the user needs to create the config.ini file
    echo Please execute the config.bat file to create the configurations before proceeding.
    pause
    exit
)


:: Get all configuration values
for /f "eol=# delims=" %%a in (config.ini) do (
    set "%%a"
)


:: Was the RELEASEDIR variable created?
if not defined RELEASEDIR (

    :: Print a message about the config issue
    echo Something is wrong with your config.ini file.
    echo Please delete your config.ini and re-execute the config.bat.
    pause
    exit
)


:: A function to choose the plugin to release
:ChoosePlugin

    :: Clear the console
    cls

    echo ======================================
    echo What plugin would you like to release?
    echo ======================================
    echo.

    :: Store a base counting variable
    set /a num=0

    :: Loop through all plugins
    for /D %%i in (*.*) do (

        :: Skip the 'packages' directory
        if %%i NEQ packages (

            :: Increment the counter
            set /a num+=1

            :: Set the current option to the current branch
            set option_!num!=%%~ni
        )
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

    set PLUGIN_NAME=!option_%choice%!

    python %STARTDIR%\packages\plugin_releaser --name=%PLUGIN_NAME%

    goto :ChooseAnother


:: A place to ask to release another plugin
:ChooseAnother
    echo.
    echo Release another plugin?

    set /p choice=

    set result=None

    if %choice% == yes set result=True
    if %choice% == y set result=True
    if %choice% == no set result=False
    if %choice% == n set result=False

    if %result% == True goto :ChoosePlugin
    if %result% == False exit
    if %result% == None goto :ChooseAnother
