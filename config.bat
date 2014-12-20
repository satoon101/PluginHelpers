@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Does the config file already exist?
if not exist %STARTDIR%\config.ini (

    echo Creating config.ini file.  Set values to your specifications.

    :: Create the PluginCreater header
    echo.
    @echo # ======================= #>> config.ini
    @echo # PLUGIN CREATER SETTINGS #>> config.ini
    @echo # ======================= #>> config.ini
    @echo.>> config.ini

    :: Create the Author variable
    echo.
    @echo # Set to your nickname.>> config.ini
    @echo # This value is used to assign the author variable when creating a plugin.>> config.ini
    @echo AUTHOR="">> config.ini
    @echo.>> config.ini

    :: Create the version control variable
    echo.
    @echo # Set to "hg" or "git" if plugins created by plugin_creater>> config.ini
    @echo #   are going to use one of the two version control systems.>> config.ini
    @echo REPOTYPE="">> config.ini
    @echo.>> config.ini
    @echo.>> config.ini

    :: Create the PluginLinker header
    echo.
    @echo # ====================== #>> config.ini
    @echo # PLUGIN LINKER SETTINGS #>> config.ini
    @echo # ====================== #>> config.ini
    @echo.>> config.ini

    :: Create the Server directory variable
    echo.
    @echo # Set to the directory that your server's are located in.>> config.ini
    @echo SERVERSTARTDIR="C:\Servers">> config.ini
    @echo.>> config.ini
    @echo.>> config.ini

    :: Create the PluginCreater header
    echo.
    @echo # ======================== #>> config.ini
    @echo # PLUGIN RELEASER SETTINGS #>> config.ini
    @echo # ======================== #>> config.ini
    @echo.>> config.ini

    :: Create the Release directory variable
    echo.
    @echo # Set to the directory where your releases should be placed.>> config.ini
    @echo RELEASEDIR="C:\Releases">> config.ini
    @echo.>> config.ini
    @echo.>> config.ini

    :: Create the SPLinker header
    echo.
    @echo # ================== #>>config.ini
    @echo # SP LINKER SETTINGS #>>config.ini    
    @echo # ================== #>>config.ini
    @echo.>> config.ini

    :: Create the Source.Python repository directory variable
    echo.
    @echo # Set to the directory where Source.Python's repository is located.>>config.ini
    @echo SOURCEPYTHONDIR="C:\Projects\Source.Python">>config.ini
    pause

) else (
    echo config.ini file already exists.  Please edit it to your liking.
    pause
)
