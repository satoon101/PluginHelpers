@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Does the config file already exist?
if exist %STARTDIR%\config.ini (

    echo config.ini file already exists.  Please edit it to your liking.
    echo If there is an error in the file, please delete it and re-run this script.

) else (

    :: Copy the default config
    type .files\config.ini .plugin_helpers\files\config.ini > config.ini
    cls
    echo Creating config.ini file.  Set values to your specifications then re-execute setup.bat.
    echo You MUST have PYTHON_EXECUTABLE defined before going further.
)

:: Link the prerequisite and exec config scrips
if not exist %STARTDIR%\exec_config.bat (
    mklink /H %STARTDIR%\exec_config.bat %STARTDIR%\.plugin_helpers\files\exec_config.bat
)
if not exist %STARTDIR%\prerequisites.bat (
    mklink /H %STARTDIR%\prerequisites.bat %STARTDIR%\.plugin_helpers\files\prerequisites.bat
)

:: Link all of the helper batch scripts
for %%F in (".plugin_helpers\packages\*.py") do (
    if not "%%~nxF"=="__init__.py" (
        if not exist %STARTDIR%\%%~nF.bat (
            mklink /H %STARTDIR%\%%~nF.bat %STARTDIR%\.plugin_helpers\files\caller.bat
        )
    )
)

pause
