# ../common/constants.py

"""Provides commonly used constants."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Platform
from platform import system

# Site-Package Imports
# Configobj
from configobj import ConfigObj
#   Path
from path import Path


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Store the platform
PLATFORM = system().lower()

# Store the package directory
PACKAGE_DIR = Path(__file__).parent.parent

# Store the main directory
START_DIR = PACKAGE_DIR.parent.parent

# Store the config file location
CONFIG_FILE = START_DIR.joinpath('config.ini')

# Get the configuration
config_obj = ConfigObj(CONFIG_FILE)

# Get a list of all plugins
plugin_list = [
    x.namebase for x in START_DIR.dirs()
    if x != PACKAGE_DIR and x.namebase != '.git']

# Store the server directory
SERVER_DIR = Path(config_obj['SERVERSTARTDIR'])

# Get a list of all servers
server_list = [
    x.namebase for x in SERVER_DIR.dirs() if x.namebase != 'steamcmd']
