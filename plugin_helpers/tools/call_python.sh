# Include exec_config
. ./plugin_helpers/tools/exec_config.sh

# Call the given package
PYTHONPATH="$STARTDIR/plugin_helpers/packages/"
export PYTHONPATH
"${PYTHONEXE}" "$STARTDIR/plugin_helpers/packages/"$(basename "${1%.**}")".py"
