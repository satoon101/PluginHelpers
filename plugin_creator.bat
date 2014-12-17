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
        echo Plugin already exists.

        :: Ask if another plugin should be created
        :CreateAnother

    :: Does the plugin not exist?
    ) else (

        :: Create the plugin
        :CreatePlugin
    )


:: A place to create the plugin
:CreatePlugin

    :: Get the plugin's directory
    PLUGINDIR=%STARTDIR%/%PLUGIN_NAME%/addons/source-python/plugins/%PLUGIN_NAME%/

    :: Create the plugin's directory
    mkdir %PLUGINDIR%

    :: Move to the plugin's directory
    cd %PLUGINDIR%

    :: Create the __init__.py file
    @echo # ../%PLUGIN_NAME%/__init__.py>> __init__.py
    @echo >> __init__.py
    @echo """""" >> __init__.py

    :: Create the info.py file
    @echo # ../%PLUGIN_NAME%/info.py>> info.py
    @echo >> info.py
    @echo # =============================================================================>> info.py
    @echo #>> info.py
    @echo # =============================================================================>> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py
    @echo >> info.py


    :: Ask if another plugin should be created
    :CreateAnother
        


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