# Include exec_config
. ./plugin_helpers/linux/exec_config.sh

# Call the given package
PYTHONPATH="$STARTDIR/plugin_helpers/packages/"
export PYTHONPATH
"${PYTHON_EXECUTABLE}" "$STARTDIR/plugin_helpers/packages/"$(basename "${1%.**}")".py"
