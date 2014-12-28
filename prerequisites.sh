# Create the prerequisite array
PREREQUISITES=(
    configobj
    path.py
    pep8
    pep257
    pyflakes
    pylint
)

# Does the config.ini file exist?
if [ ! -f config.ini ]; then
    echo No config.ini file found.
    echo Please execute the config.sh file to create the config.ini before proceeding.
    exit
fi

# Execute the config.ini file to declare the variables
. ./config.ini

if [ ! -n "${PYTHONEXE}" ]; then
    echo Something is wrong with your config.ini file.
    echo Please delete your config.ini file and re-execute config.sh.
    exit
fi

for i in "${PREREQUISITES[@]}"
do

    # Print a message about the prerequisite being installed
    echo Attempting to install/upgrade "$i".
    echo ""

    # Install the prerequisite
    ${PYTHONEXE} -m pip install --upgrade %i

    echo ""

done
