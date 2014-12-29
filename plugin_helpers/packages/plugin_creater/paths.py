# ../plugin_creater/paths.py

"""Stores paths used by plugin_creater."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Site-Package Imports
#   Path
from path import Path


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Store the base directory to create plugins in
STARTDIR = Path(__file__).parent.parent.parent

# Store the config file path
CONFIG_FILE = STARTDIR.joinpath('config.ini')
