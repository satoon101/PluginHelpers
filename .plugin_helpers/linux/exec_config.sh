# Store the current directory for later use
STARTDIR="$PWD"

# Does the config.ini file exist?
if [ ! -f config.ini ]; then
    echo No config.ini file found.
    echo Please execute the setup.sh file to create the config.ini before proceeding.
    exit 1
fi

# Execute the config.ini file to declare the variables
. ./config.ini

# Is PYTHON_EXECUTABLE define in the config?
if [ ! -n "${PYTHON_EXECUTABLE}" ]; then
    echo Something is wrong with your config.ini file.
    echo Please delete your config.ini file and re-execute setup.sh.
    exit 1
fi
