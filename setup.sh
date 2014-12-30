# Store the start directory for later reference
STARTDIR="$PWD"

# Does the config file already exist?
if [ -f $STARTDIR/config.ini ]; then

    echo config.ini file already exists.  Please edit it to your liking.

else

    echo Creating config.ini file.  Set values to your specifications.
    cp plugin_helpers/linux/config.ini config.ini

fi

echo ""
echo ""

# Loop through all hooks
for filename in $STARTDIR/plugin_helpers/hooks/*; do

    # Does the hook's link exist?
    if [ ! -f $STARTDIR/.git/hooks/$(basename "$filename") ]; then

        # Create the hook
        ln $filename $STARTDIR/.git/hooks/$(basename "$filename")

    fi
done

# Get the current git branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Force a checkout to execute the checkout hook
git checkout $CURRENT_BRANCH
