# Include exec_config
. ./plugin_helpers/tools/exec_config.sh

# Create the prerequisite array
PREREQUISITES=(
    configobj
    path.py
    pep8
    pep257
    pyflakes
    pylint
)

for i in "${PREREQUISITES[@]}"; do

    # Print a message about the prerequisite being installed
    echo Attempting to install/upgrade "$i".
    echo ""

    # Install the prerequisite
    ${PYTHONEXE} -m pip install --upgrade %i

    echo ""

done
