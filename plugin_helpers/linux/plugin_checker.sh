# Execute the configuration
sh exec_config.sh || exit

# Call the plugin checker
${PYTHONEXE} $STARTDIR/plugin_helpers/packages/plugin_checker
