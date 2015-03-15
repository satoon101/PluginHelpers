# ../$plugin_name/info.py

"""Provides/stores information about the plugin."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python Imports
#   Cvars
from cvars.public import PublicConVar
#   Plugins
from plugins.info import PluginInfo


# =============================================================================
# >> PLUGIN INFO
# =============================================================================
info = PluginInfo()
info.name = '$plugin_title'
info.author = '$author'
info.version = '1.0'
info.basename = '$plugin_name'
info.variable = info.basename + '_version'
info.url = ''
info.convar = PublicConVar(
    info.variable, info.version, 0, info.name + ' Version')
