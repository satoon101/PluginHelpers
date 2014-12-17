@echo off


:: =================== ::
:: >> CONFIGURATION >> ::
:: =================== ::


:: Set to the directory where the server's are located
set SERVERSTARTDIR=D:\Servers


:: ==================== ::
:: END OF CONFIGURATION ::
:: ==================== ::


:: Set the start directory for later reference
set STARTDIR=%CD%


:: Allow the use of delayed expansion
setlocal EnableDelayedExpansion


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

    :: Get the server's data directory
    set SERVERDATADIR=%SERVERDIR%\addons\source-python\data\plugins

    :: Get the server's cfg directory
    set SERVERCFGDIR=%SERVERDIR%\cfg\source-python

    :: Get the server's translations directory
    set SERVERTRANSLATIONSDIR=%SERVERDIR%\resource\source-python\translations

    :: Loop through all plugins
    for /D %%i in (*.*) do (

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


            :: Does the plugin's cfg directory exist?
            if exist %STARTDIR%\%%~ni\cfg\%%~ni (

                :: Is the cfg directory already linked?
                if exist %SERVERCFGDIR%\%%~ni (

                    :: Print a message to notify the cfg directory is already linked
                    echo     Cfg directory already linked.

                ) else (

                    :: Print a message to notify the cfg directory is being linked
                    echo     Linking cfg directory.

                    echo.
                    :: Create the symbolic link to the directory
                    mklink /J %SERVERCFGDIR%\%%~ni %STARTDIR%\%%~ni\cfg\%%~ni
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
    pause


:: ======================================== ::
:: >> Create a symbolic link to a folder >> ::
:: ======================================== ::
:: mklink /J link_directory directory_to_link

:: ====================================== ::
:: >> Create a symbolic link to a file >> ::
:: ====================================== ::
:: mklink /H link_file file_to_link