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


:: A function to choose the server
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

    :: If the choice is valid, create links for the server
    goto :CreateLinks


:: A place to create links for the server
:CreateLinks

    :: Get the server's directory
    set SERVERDIR=%SERVERSTARTDIR%\%SERVER_NAME%\%SERVER_NAME%

    :: Get the server's plugins directory
    set SERVERPLUGINDIR=%SERVERDIR%\addons\source-python\plugins

    :: Get the server's cfg directory
    set SERVERCFGDIR=%SERVERDIR%\cfg\source-python

    :: Get the server's data directory
    set SERVERDATADIR=%SERVERDIR%\addons\source-python\data\plugins

    :: Get the server's events directory
    set SERVEREVENTSDIR=%SERVERDIR%\resource\source-python\events

    :: Get the server's logs directory
    set SERVERLOGSDIR=%SERVERDIR%\logs\source-python

    :: Get the server's sounds directory
    set SERVERSOUNDDIR=%SERVERDIR%\sound\source-python

    :: Get the server's translations directory
    set SERVERTRANSLATIONSDIR=%SERVERDIR%\resource\source-python\translations

    :: Loop through all plugins
    for /D %%i in (*.*) do (

        :: Skip the 'packages' directory
        if %%i NEQ packages (

            :: Does the plugin's plugin directory exist?
            if exist %STARTDIR%\%%~ni\addons\source-python\plugins\%%~ni (

                :: Print a message the the plugin is being linked
                echo %%~ni is being linked to %SERVER_NAME%.

                :: Is the plugin already linked?
                if exist %SERVERPLUGINDIR%\%%~ni (

                    :: Print a message to notify the plugin is already linked
                    echo     Plugin already linked.

                ) else (

                    echo.
                    :: Create the symbolic link to the directory
                    mklink /J %SERVERPLUGINDIR%\%%~ni %STARTDIR%\%%~ni\addons\source-python\plugins\%%~ni
                    echo.
                )


                :: Does the plugin's cfg directory exist?
                if exist %STARTDIR%\%%~ni\cfg\source-python\%%~ni (

                    :: Is the cfg directory already linked?
                    if exist %SERVERCFGDIR%\%%~ni (

                        :: Print a message to notify the cfg directory is already linked
                        echo     Cfg directory already linked.

                    ) else (

                        :: Print a message to notify the cfg directory is being linked
                        echo     Linking cfg directory.

                        echo.
                    :: Create the symbolic link to the directory
                    mklink /J %SERVERCFGDIR%\%%~ni %STARTDIR%\%%~ni\cfg\source-python\%%~ni
                    echo.
                    )
                )


                :: Does the plugin's data directory exist?
                if exist %STARTDIR%\%%~ni\addons\source-python\data\plugins\%%~ni (

                    :: Is the data directory already linked?
                    if exist %SERVERDATADIR%\%%~ni (

                        :: Print a message to notify the data directory is already linked
                        echo     Data directory already linked.

                    ) else (

                        :: Print a message to notify the data directory is being linked
                        echo     Linking data directory.

                        echo.
                        :: Create the symbolic link to the directory
                        mklink /J %SERVERDATADIR%\%%~ni %STARTDIR%\%%~ni\addons\source-python\data\plugins\%%~ni
                        echo.
                    )
                )


                :: Does the plugin's data file exist?
                if exist %STARTDIR%\%%~ni\addons\source-python\data\plugins\%%~ni.ini (

                    :: Is the data file already linked?
                    if exist %SERVERDATADIR%\%%~ni.ini (

                        :: Print a message to notify the data file is already linked
                        echo     Data file already linked.

                    ) else (

                        :: Print a message to notify the data file is being linked
                        echo     Linking data file.

                        echo.
                        :: Create the symbolic link to the file
                        mklink /H %SERVERDATADIR%\%%~ni.ini %STARTDIR%\%%~ni\addons\source-python\data\plugins\%%~ni.ini
                        echo.
                    )
                )


                :: Does the plugin's events directory exist?
                if exist %STARTDIR%\%%~ni\resource\source-python\events\%%~ni (

                    :: Is the events directory already linked?
                    if exist %SERVEREVENTSDIR%\%%~ni (

                        :: Print a message to notify the events directory is already linked
                        echo     Events directory already linked.

                    ) else (

                        :: Print a message to notify the events directory is being linked
                        echo     Linking events directory.

                        echo.
                        :: Create the symbolic link to the directory
                        mklink /J %SERVEREVENTSDIR%\%%~ni %STARTDIR%\%%~ni\resource\source-python\events\%%~ni
                        echo.
                    )
                )


                :: Does the plugin's logs directory exist?
                if exist %STARTDIR%\%%~ni\logs\source-python\%%~ni (

                    :: Is the logs directory already linked?
                    if exist %SERVERLOGSDIR%\%%~ni (

                        :: Print a message to notify the logs directory is already linked
                        echo     Logs directory already linked.

                    ) else (

                        :: Print a message to notify the logs directory is being linked
                        echo     Linking logs directory.

                        echo.
                        :: Create the symbolic link to the directory
                        mklink /J %SERVERLOGSDIR%\%%~ni %STARTDIR%\%%~ni\logs\source-python\%%~ni
                        echo.
                    )
                )


                :: Does the plugin's sound directory exist?
                if exist %STARTDIR%\%%~ni\sound\source-python\%%~ni (

                    :: Is the sound directory already linked?
                    if exist %SERVERSOUNDDIR%\%%~ni (

                        :: Print a message to notify the sound directory is already linked
                        echo     Sound directory already linked.

                    ) else (

                        :: Print a message to notify the sound directory is being linked
                        echo     Linking sound directory.

                        echo.
                        :: Create the symbolic link to the directory
                        mklink /J %SERVERSOUNDDIR%\%%~ni %STARTDIR%\%%~ni\sound\source-python\%%~ni
                        echo.
                    )
                )


                :: Does the plugin's translations directory exist?
                if exist %STARTDIR%\%%~ni\resource\source-python\translations\%%~ni (

                    :: Is the translations directory already linked?
                    if exist %SERVERTRANSLATIONSDIR%\%%~ni (

                        :: Print a message to notify the translations directory is already linked
                        echo     Translations directory already linked.

                    ) else (

                        :: Print a message to notify the translations directory is being linked
                        echo     Linking translations directory.

                        echo.
                        :: Create the symbolic link to the directory
                        mklink /J %SERVERTRANSLATIONSDIR%\%%~ni %STARTDIR%\%%~ni\resource\source-python\translations\%%~ni
                        echo.
                    )
                )


                :: Does the plugin's translations file exist?
                if exist %STARTDIR%\%%~ni\resource\source-python\translations\%%~ni.ini (

                    :: Is the translations file already linked?
                    if exist %SERVERTRANSLATIONSDIR%\%%~ni.ini (

                        :: Print a message to notify the translations file is already linked
                        echo     Translations file already linked.

                    ) else (

                        :: Print a message to notify the translations file is being linked
                        echo     Linking translations file.

                        echo.
                        :: Create the symbolic link to the file
                        mklink /H %SERVERTRANSLATIONSDIR%\%%~ni.ini %STARTDIR%\%%~ni\resource\source-python\translations\%%~ni.ini
                        echo.
                    )
                )

            ) else (

                :: Print a message the the plugin cannot be linked
                echo %%~ni cannot be linked.

            )

            :: Print a blank line between plugins
            echo.

        )
    )
    pause
