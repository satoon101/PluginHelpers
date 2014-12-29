# Execute the configuration
sh exec_config.sh || exit

# Call the plugin linker
${PYTHONEXE} $STARTDIR/plugin_helpers/packages/plugin_linker
