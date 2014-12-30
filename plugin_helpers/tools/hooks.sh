# Store the current directory for later use
STARTDIR="$PWD"

# Is the operating system Windows?
if [ "$OSTYPE" == "msys" ]; then
    DIRECTORY='windows'

# Is the operating system Linux?
else
    DIRECTORY='linux'
fi

# Loop through all files to link
for filename in ./plugin_helpers/$DIRECTORY/*; do

    # Skip "config.ini" as that needs to not be linked
    if [ "$(basename "$filename")" != config.ini ]; then

        # Does the link not yet exist?
        if [ ! -f "$STARTDIR/$(basename "$filename")" ]; then

            # Create the link
            ln $filename "$STARTDIR/$(basename "$filename")"

        fi
    fi
done
