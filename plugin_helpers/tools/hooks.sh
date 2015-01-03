# Store the current directory for later use
STARTDIR="$PWD"

# Store the Python files to not make callers to
PYTHON_EXCEPTIONS=("__init__" "constants" "functions")

# A function to get whether a file name is in the Python Exceptions array
function should_create_caller () {

    local n=$#
    local value=${!n}
    for ((i=1;i < $#;i++)) {
        if [ "${!i}" == "${value}" ]; then
            echo "y"
            return 0
        fi
    }
    echo "n"
    return 1
}

# Is the operating system Windows?
if [ "$OSTYPE" == "msys" ]; then
    DIRECTORY='windows'
    EXTENSION='bat'

# Is the operating system Linux?
else
    DIRECTORY='linux'
    EXTENSION='sh'
fi

# Link the prerequisite file
cp ./plugin_helpers/$DIRECTORY/prerequisites.$EXTENSION $STARTDIR/prerequisites.$EXTENSION

# Loop through all Python files
for filename in ./plugin_helpers/packages/*; do

    # Link a caller for the file if necessary
    if [ ! $(should_create_caller "${PYTHON_EXCEPTIONS[@]}" "$(basename "${filename%.*}")") == "y" ]; then
        if [ ! "$(basename "${filename%.**}")" == "" ]; then
            ln ./plugin_helpers/$DIRECTORY/caller.$EXTENSION ./"$(basename "${filename%.*}")".$EXTENSION
        fi
    fi
done
