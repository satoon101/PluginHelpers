@echo off

:: Set the start directory for later reference
set STARTDIR="%CD%"

:: Create the batch array
set BATCH_ARRAY[0]="plugin_checker"
set BATCH_ARRAY[1]="plugin_creater"
set BATCH_ARRAY[2]="plugin_linker"
set BATCH_ARRAY[3]="plugin_releaser"
set BATCH_ARRAY[4]="prerequisites"
set BATCH_ARRAY[5]="sp_linker"

:: Loop through all batch files
for /F "tokens=2 delims==" %%s in ('set BATCH_ARRAY[') do (

    :: Copy the file
    copy plugin_helpers\windows\%%s.bat %%s.bat
)

:: Does the config file already exist?
if not exist %STARTDIR%\config.ini (

    echo Creating config.ini file.  Set values to your specifications.

    :: Copy the default config
    copy plugin_helpers\windows\defaults.ini config.ini
)
