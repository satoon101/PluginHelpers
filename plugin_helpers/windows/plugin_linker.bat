@echo off


:: Set the start directory for later reference
set STARTDIR="%CD%"


:: Allow the use of delayed expansion
setlocal EnableDelayedExpansion


:: Has the config.ini file been created?
if not exist %STARTDIR%\config.ini (

    :: Print a message that the user needs to create the config.ini file
    echo Please execute the config.bat file to create the config.ini before proceeding.
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
    echo Please delete your config.ini file and re-execute the config.bat.
    pause
    exit
)


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

    :: If the choice is valid, ask which plugin to link
    goto :ChoosePlugin


:: A place to choose a plugin
:ChoosePlugin

    :: Clear the console
    cls

    echo ===================================
    echo What plugin would you like to link?
    echo ===================================
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

    :: Increment the counter
    set /a num+=1

    :: Add an option to link 'all' plugins
    set option_!num!=ALL

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
    set PLUGIN_NAME=!option_%choice%!

    :: Should all servers be linked?
    if %SERVER_NAME% == ALL (

        :: Loop through all servers
        for /D %%i in (%SERVERSTARTDIR%\*.*) do (

            :: Do not include 'steamcmd' directory
            if %%~ni NEQ steamcmd (

                :: Link the plugin(s) to the server
                call :LinkServer %%~ni %PLUGIN_NAME%

            )

        )

    ) else (

        :: Link the plugin(s) to the selected server
        call :LinkServer %SERVER_NAME% %PLUGIN_NAME%

    )

    pause
    exit


:: A place to start linking a server for plugins
:LinkServer

    :: Should all plugins be linked to the server?
    if %2 == ALL (

        :: Loop through all plugins
        for /D %%i in (*.*) do (

            :: Skip the 'packages' directory
            if %%i NEQ packages (

                :: Link the plugin to the server
                call :LinkPlugin %1 %%~ni

                :: Create two blank lines between plugins
                echo.
                echo.

            )

        )

    ) else (

        :: Link the selected plugin to the server
        call :LinkPlugin %1 %2

    )
    goto :eof



:: A place to create links for the server
:LinkPlugin

    :: Get the server's directory
    set SERVERDIR=%SERVERSTARTDIR%\%1\%1

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

    :: Does the plugin's plugin directory exist?
    if exist %STARTDIR%\%2\addons\source-python\plugins\%2 (

        :: Print a message the the plugin is being linked
        echo %2 is being linked to %1.

        :: Is the plugin already linked?
        if exist %SERVERPLUGINDIR%\%2 (

            :: Print a message to notify the plugin is already linked
            echo     Plugin already linked.

        ) else (

            echo.
            :: Create the symbolic link to the directory
            mklink /J %SERVERPLUGINDIR%\%2 %STARTDIR%\%2\addons\source-python\plugins\%2
            echo.
        )


        :: Does the plugin's cfg directory exist?
        if exist %STARTDIR%\%2\cfg\source-python\%2 (

            :: Is the cfg directory already linked?
            if exist %SERVERCFGDIR%\%2 (

                :: Print a message to notify the cfg directory is already linked
                echo     Cfg directory already linked.

            ) else (

                :: Print a message to notify the cfg directory is being linked
                echo     Linking cfg directory.

                echo.
            :: Create the symbolic link to the directory
            mklink /J %SERVERCFGDIR%\%2 %STARTDIR%\%2\cfg\source-python\%2
            echo.
            )
        )


        :: Does the plugin's data directory exist?
        if exist %STARTDIR%\%2\addons\source-python\data\plugins\%2 (

            :: Is the data directory already linked?
            if exist %SERVERDATADIR%\%2 (

                :: Print a message to notify the data directory is already linked
                echo     Data directory already linked.

            ) else (

                :: Print a message to notify the data directory is being linked
                echo     Linking data directory.

                echo.
                :: Create the symbolic link to the directory
                mklink /J %SERVERDATADIR%\%2 %STARTDIR%\%2\addons\source-python\data\plugins\%2
                echo.
            )
        )


        :: Does the plugin's data file exist?
        if exist %STARTDIR%\%2\addons\source-python\data\plugins\%2.ini (

            :: Is the data file already linked?
            if exist %SERVERDATADIR%\%2.ini (

                :: Print a message to notify the data file is already linked
                echo     Data file already linked.

            ) else (

                :: Print a message to notify the data file is being linked
                echo     Linking data file.

                echo.
                :: Create the symbolic link to the file
                mklink /H %SERVERDATADIR%\%2.ini %STARTDIR%\%2\addons\source-python\data\plugins\%2.ini
                echo.
            )
        )


        :: Does the plugin's events directory exist?
        if exist %STARTDIR%\%2\resource\source-python\events\%2 (

            :: Is the events directory already linked?
            if exist %SERVEREVENTSDIR%\%2 (

                :: Print a message to notify the events directory is already linked
                echo     Events directory already linked.

            ) else (

                :: Print a message to notify the events directory is being linked
                echo     Linking events directory.

                echo.
                :: Create the symbolic link to the directory
                mklink /J %SERVEREVENTSDIR%\%2 %STARTDIR%\%2\resource\source-python\events\%2
                echo.
            )
        )


        :: Does the plugin's logs directory exist?
        if exist %STARTDIR%\%2\logs\source-python\%2 (

            :: Is the logs directory already linked?
            if exist %SERVERLOGSDIR%\%2 (

                :: Print a message to notify the logs directory is already linked
                echo     Logs directory already linked.

            ) else (

                :: Print a message to notify the logs directory is being linked
                echo     Linking logs directory.

                echo.
                :: Create the symbolic link to the directory
                mklink /J %SERVERLOGSDIR%\%2 %STARTDIR%\%2\logs\source-python\%2
                echo.
            )
        )


        :: Does the plugin's sound directory exist?
        if exist %STARTDIR%\%2\sound\source-python\%2 (

            :: Is the sound directory already linked?
            if exist %SERVERSOUNDDIR%\%2 (

                :: Print a message to notify the sound directory is already linked
                echo     Sound directory already linked.

            ) else (

                :: Print a message to notify the sound directory is being linked
                echo     Linking sound directory.

                echo.
                :: Create the symbolic link to the directory
                mklink /J %SERVERSOUNDDIR%\%2 %STARTDIR%\%2\sound\source-python\%2
                echo.
            )
        )


        :: Does the plugin's translations directory exist?
        if exist %STARTDIR%\%2\resource\source-python\translations\%2 (

            :: Is the translations directory already linked?
            if exist %SERVERTRANSLATIONSDIR%\%2 (

                :: Print a message to notify the translations directory is already linked
                echo     Translations directory already linked.

            ) else (

                :: Print a message to notify the translations directory is being linked
                echo     Linking translations directory.

                echo.
                :: Create the symbolic link to the directory
                mklink /J %SERVERTRANSLATIONSDIR%\%2 %STARTDIR%\%2\resource\source-python\translations\%2
                echo.
            )
        )


        :: Does the plugin's translations file exist?
        if exist %STARTDIR%\%2\resource\source-python\translations\%2.ini (

            :: Is the translations file already linked?
            if exist %SERVERTRANSLATIONSDIR%\%2.ini (

                :: Print a message to notify the translations file is already linked
                echo     Translations file already linked.

            ) else (

                :: Print a message to notify the translations file is being linked
                echo     Linking translations file.

                echo.
                :: Create the symbolic link to the file
                mklink /H %SERVERTRANSLATIONSDIR%\%2.ini %STARTDIR%\%2\resource\source-python\translations\%2.ini
                echo.
            )
        )

    ) else (

        :: Print a message the the plugin cannot be linked
        echo %2 cannot be linked.

    )
