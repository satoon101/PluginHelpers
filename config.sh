# Store the start directory for later reference
STARTDIR="$PWD"

# Does the config file already exist?
if [ -f $STARTDIR/config.ini ]; then

    echo Creating config.ini file.  Set values to your specifications.
    cp plugin_helpers/linux-defaults.ini config.ini

else

    echo config.ini file already exists.  Please edit it to your liking.

fi
