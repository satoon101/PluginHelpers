# Execute the configuration
sh exec_config.sh || exit

# Call the plugin releaser
${PYTHONEXE} $STARTDIR/plugin_helpers/packages/plugin_releaser
