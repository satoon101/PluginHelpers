# Execute the configuration
sh exec_config.sh || exit

# Call the Source.Python linker
${PYTHONEXE} $STARTDIR/plugin_helpers/packages/sp_linker
