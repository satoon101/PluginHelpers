@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Allow the use of delayed expansion
setlocal EnableDelayedExpansion


:: A function to name the new plugin
:NamePlugin

    :: Clear the console
    cls

    echo ===============================
    echo What is the name of the plugin?
    echo ===============================
    echo.

    :: Request input
    set /p PLUGIN_NAME=

    set "var="&for /f "delims=0123456789_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" %%i in ("%PLUGIN_NAME%") do set var=%%i
    if defined var (

        echo Invalid plugin name "%PLUGIN_NAME%"
        goto :CreateAnother

    )

    :: Does the plugin already exist?
    if exist %STARTDIR%/%PLUGIN_NAME% (

        :: Notify that the plugin already exists
        echo Plugin "%PLUGIN_NAME%" already exists.

        :: Ask to create another plugin
        goto :CreateAnother

    )

    :: Create the argument string
    set ARGUMENT_STRING=

    :: Ask if a cfg directory should be included
    goto :CreateCfg


:: A place to ask to create a plugin
:CreateAnother

    :: Ask to create another plugin
    echo.
    echo Create another plugin?

    :: Request a choice
    set /p choice=

    :: Set a base value for the result
    set result=None

    :: Get the result
    if %choice% == yes set result=True
    if %choice% == y set result=True
    if %choice% == no set result=False
    if %choice% == n set result=False

    :: Determine what to do with the result
    if %result% == True goto :NamePlugin
    if %result% == False exit
    if %result% == None (
        cls
        goto :CreateAnother
    )


::
:CreateCfg

    :: Ask if the cfg directory should be added
    cls
    echo Should a ..\cfg\source-python\%PLUGIN_NAME% directory be added?

    :: Print the choices
    echo.
    echo     (1) Yes
    echo     (2) No

    :: Request a choice
    set /p choice=

    :: Set a base value for the result
    set result=None

    :: Get the result
    if %choice% == 1 set result=True
    if %choice% == 2 set result=False

    :: Determine what to do with the result
    if %result% == True (

        set ARGUMENT_STRING=%ARGUMENT_STRING% --config
    )

    if %result% == None (
        goto :CreateCfg

    ) else (

        :: Ask about data
        goto :CreateData
    )



::
:CreateData

    :: Ask if the data directory or file should be added
    cls
    echo Should an ..\data\plugins\%PLUGIN_NAME% directory or ..\data\plugins\%PLUGIN_NAME%.ini file be added?

    :: Print the choices
    echo.
    echo     (0) No, neither should be added.
    echo     (1) Yes, a directory should be added.
    echo     (2) Yes, a file should be added.

    :: Request a choice
    set /p choice=

    :: Set a base value for the result
    set result=None

    :: Get the result
    if %choice% == 0 set result=False
    if %choice% == 1 (

        set result=True
        set ARGUMENT_STRING=%ARGUMENT_STRING% --data=directory
    )

    if %choice% == 2 (

        set result=True
        set ARGUMENT_STRING=%ARGUMENT_STRING% --data=file
    )

    :: Was the result invalid?
    if %result% == None (
        goto :CreateData

    ) else (

        :: Ask about events
        goto :CreateEvents
    )


::
:CreateEvents

    :: Ask if the events directory should be added
    cls
    echo Should a ..\resource\source-python\events\source-python\%PLUGIN_NAME% directory be added?

    :: Print the choices
    echo.
    echo     (1) Yes
    echo     (2) No

    :: Request a choice
    set /p choice=

    :: Set a base value for the result
    set result=None

    :: Get the result
    if %choice% == 1 set result=True
    if %choice% == 2 set result=False

    :: Determine what to do with the result
    if %result% == True (

        set ARGUMENT_STRING=%ARGUMENT_STRING% --events
    )

    if %result% == None (
        goto :CreateEvents

    ) else (

        :: Ask about logs
        goto :CreateLogs
    )


::
:CreateLogs

    :: Ask if the logs directory should be added
    cls
    echo Should a ..\logs\source-python\%PLUGIN_NAME% directory be added?

    :: Print the choices
    echo.
    echo     (1) Yes
    echo     (2) No

    :: Request a choice
    set /p choice=

    :: Set a base value for the result
    set result=None

    :: Get the result
    if %choice% == 1 set result=True
    if %choice% == 2 set result=False

    :: Determine what to do with the result
    if %result% == True (

        set ARGUMENT_STRING=%ARGUMENT_STRING% --logs
    )

    if %result% == None (
        goto :CreateLogs

    ) else (

        :: Ask about data
        goto :CreateSound
    )


::
:CreateSound

    :: Ask if the sound directory should be added
    cls
    echo Should a ..\sound\source-python\%PLUGIN_NAME% directory be added?

    :: Print the choices
    echo.
    echo     (1) Yes
    echo     (2) No

    :: Request a choice
    set /p choice=

    :: Set a base value for the result
    set result=None

    :: Get the result
    if %choice% == 1 set result=True
    if %choice% == 2 set result=False

    :: Determine what to do with the result
    if %result% == True (

        set ARGUMENT_STRING=%ARGUMENT_STRING% --sound
    )

    if %result% == None (
        goto :CreateSound

    ) else (

        :: Ask about data
        goto :CreateTranslations
    )


::
:CreateTranslations

    :: Ask if the translations directory or file should be added
    cls
    echo Should an ..\resource\source-python\translations\%PLUGIN_NAME% directory or ..\resource\source-python\translations\%PLUGIN_NAME%.ini file be added?

    :: Print the choices
    echo.
    echo     (0) No, neither should be added.
    echo     (1) Yes, a directory should be added.
    echo     (2) Yes, a file should be added.

    :: Request a choice
    set /p choice=

    :: Set a base value for the result
    set result=None

    :: Get the result
    if %choice% == 0 set result=False
    if %choice% == 1 (

        set result=True
        set ARGUMENT_STRING=%ARGUMENT_STRING% --translations=directory
    )

    if %choice% == 2 (

        set result=True
        set ARGUMENT_STRING=%ARGUMENT_STRING% --translations=file
)

    :: Was the result invalid?
    if %result% == None (
        goto :CreateTranslations

    ) else (

        :: Ask about translations
        goto :CallPython
    )


::
:CallPython

    :: Create the plugin
    python %STARTDIR%\packages\plugin_creater --name="%PLUGIN_NAME%"%ARGUMENT_STRING%

    pause
