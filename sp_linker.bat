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


:: Was the SERVERSTARTDIR variable created?
if not defined SERVERSTARTDIR (

    :: Print a message about the config issue
    echo Something is wrong with your config.ini file.
    echo Please delete your config.ini and re-execute the config.bat.
    pause
    exit
)


:: Was the SOURCEPYTHONDIR variable created?
if not defined SOURCEPYTHONDIR (

    :: Print a message about the config issue
    echo Something is wrong with your config.ini file.
    echo Please delete your config.ini and re-execute the config.bat.
    pause
    exit
)


:: Create the directory array
set DIRECTORIES[0]="addons"
set DIRECTORIES[1]="cfg"
set DIRECTORIES[2]="logs"
set DIRECTORIES[3]="resource"
set DIRECTORIES[4]="sound"


:: A place to choose the server
:ChooseServer

    :: Clear the console
    cls

    echo ====================================
    echo Which server would you like to link?
    echo ====================================
    echo.

    :: Store a base counting variable
    set /a num=0

    :: Loop through all servers
    for /D %%i in (%SERVERSTARTDIR%\*.*) do (

        :: Do not include 'steamcmd' directory
        if %%~ni NEQ steamcmd (

            :: Increment the counter
            set /a num+=1

            :: Set the current option to the current server
            set option_!num!=%%~ni
        )
    )

    :: Increment the counter
    set /a num+=1

    :: Add an option to link 'all' servers
    set option_!num!=ALL

    :: Loop through the options
    for /l %%a in (1, 1, %num%) do (

        :: Print the option to the console
        echo    (%%a^^^) !option_%%a!
    )

    echo.

    :: Request a choice of server
    set /p choice=

    :: Was the choice invalid?
    if %choice% leq 0 goto :ChooseServer
    if %choice% gtr %num% goto :ChooseServer

    :: Set the server value to the choice
    set SERVER_NAME=!option_%choice%!

    :: Should all servers be linked?
    if %SERVER_NAME% == ALL (

        :: Loop through all servers
        for /D %%i in (%SERVERSTARTDIR%\*.*) do (

            :: Do not include 'steamcmd' directory
            if %%~ni NEQ steamcmd (

                :: Link Source.Python to the server
                call :LinkServer %%~ni

            )

        )

    ) else (

        :: Link Source.Python to the selected server
        call :LinkServer %SERVER_NAME%

    )

    pause
    exit


:: A place to link Source.Python to a server
:LinkServer

    :: Loop through all directories to link
    for /F "tokens=2 delims==" %%s in ('set DIRECTORIES[') do (

        :: Create the base directory if it doesn't exist
        if not exist %SERVERSTARTDIR%\%1\%1\%%~ns (

            mkdir %SERVERSTARTDIR%\%1\%1\%%~ns
        )

        :: Does the source-python directory exist in the base directory?
        if exist %SERVERSTARTDIR%\%1\%1\%%~ns\source-python (

            echo Cannot link %SERVERSTARTDIR%\%1\%1\%%~ns\source-python, directory already exists.

        ) else (

            echo.
            mklink /J %SERVERSTARTDIR%\%1\%1\%%~ns\source-python %SOURCEPYTHONDIR%\%%~ns\source-python
            echo.

        )

    )

    goto :eof
