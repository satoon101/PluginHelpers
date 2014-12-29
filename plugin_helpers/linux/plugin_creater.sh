# Execute the configuration
sh exec_config.sh || exit

# Call the plugin creater
${PYTHONEXE} $STARTDIR/plugin_helpers/packages/plugin_creater
