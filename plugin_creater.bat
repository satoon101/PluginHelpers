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

    :: Does the plugin already exist?
    if exist %STARTDIR%/%PLUGIN_NAME% (

        :: Notify that the plugin already exists
        echo Plugin "%PLUGIN_NAME%" already exists.

    ) else (

        :: Create the argument string
        set ARGUMENT_STRING=""

        :: Ask if a cfg directory should be included
        goto :CreateCfg
    )

    :: Ask to create another plugin
    goto :CreateAnother


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
    echo Should a ..\cfg\source-python\%PLUGIN_NAME% be added?

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
    if %result% == True set ARGUMENT_STRING=%ARGUMENT_STRING% --config
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
    if %choice% == 1 set result=" --data=directory"
    if %choice% == 2 set result=" --data=file"

    :: Was the result invalid?
    if %result% == None (
        goto :CreateData

    ) else (

        :: Should a directory or file be added?
        if %result% NEQ False set ARGUMENT_STRING=%ARGUMENT_STRING%%result%

        :: Ask about translations
        goto :CreateTranslations
    )


::
:CreateTranslations

    :: Ask if the translations directory or file should be added
    cls
    echo Should an ..\translations\%PLUGIN_NAME% directory or ..\translations\%PLUGIN_NAME%.ini file be added?

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
    if %choice% == 1 set result=" --translations=directory"
    if %choice% == 2 set result=" --translations=file"

    :: Was the result invalid?
    if %result% == None (
        goto :CreateTranslations

    ) else (

        :: Should a directory or file be added?
        if %result% NEQ False set ARGUMENT_STRING=%ARGUMENT_STRING%%result%

        :: Ask about translations
        goto :CallPython
    )


::
:CallPython

    :: Create the plugin
    python packages\plugin_creater %PLUGIN_NAME%%ARGUMENT_STRING%

    :: Print message that the plugin was created
    echo Plugin "%PLUGIN_NAME%" created successfully.

    pause
