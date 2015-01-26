# ../constants.py

"""Provides commonly used constants."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Platform
from platform import system

# Site-Package Imports
#   Configobj
from configobj import ConfigObj
#   Path
from path import Path


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Store the platform
PLATFORM = system().lower()

# Store the binary extension
BINARY_EXTENSION = 'dll' if PLATFORM == 'windows' else 'so'

# Store the main directory
START_DIR = Path(__file__).parent.parent.parent.parent

# Get the configuration
config_obj = ConfigObj(START_DIR.joinpath('config.ini'))

# Store the server directory
SERVER_DIR = Path(config_obj['SERVERSTARTDIR'])

# Store the Source.Python repository directory
SOURCE_PYTHON_DIR = Path(config_obj['SOURCEPYTHONDIR'])

# Get Source.Python's addons directory
SOURCE_PYTHON_ADDONS_DIR = SOURCE_PYTHON_DIR.joinpath(
    'addons', 'source-python')

# Get Source.Python's build directory
SOURCE_PYTHON_BUILDS_DIR = SOURCE_PYTHON_DIR.joinpath('src', 'Builds')

# Get the directories to link
source_python_directories = [
    x.namebase for x in SOURCE_PYTHON_DIR.dirs()
    if x.namebase not in ('addons', 'src', '.git')]

# Get the addons directories to link
source_python_addons_directories = [
    x.namebase for x in SOURCE_PYTHON_DIR.joinpath(
        'addons', 'source-python').dirs() if x.namebase != 'bin']

# Store the Steam directory
STEAM_DIRS = {
    Path(directory).joinpath('SteamApps')
    for directory in config_obj['STEAMDIRS'].split(';')}

# Store the Release directory
RELEASE_DIR = Path(config_obj['RELEASEDIR'])

# Store the Python executable path
PYTHON_EXE = config_obj['PYTHONEXE']

# Get a list of all plugins
plugin_list = [
    x.namebase for x in START_DIR.dirs()
    if x.namebase not in ('plugin_helpers', '.git')]

# Get a list of all servers
server_list = [
    x.namebase for x in SERVER_DIR.dirs() if x.namebase != 'steamcmd']

# Get the supported games
supported_games = ConfigObj(
    START_DIR.joinpath('plugin_helpers', 'tools', 'games.ini'))

# Get the game directories
game_directories = {}
for _folder in supported_games:
    game_directories.update(supported_games[_folder])

# Get the supported builds
supported_builds = ConfigObj(
    START_DIR.joinpath('plugin_helpers', 'tools', 'builds.ini'))


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def _get_available_games():
    """Yield available games with their paths."""
    # Loop through each Steam directory
    for steam_dir in STEAM_DIRS:

        # Loop through each internal Steam directory to support
        for directory in supported_games:

            # Get the full path to the current directory
            current_directory = steam_dir.joinpath(directory)

            # Loop through all supported games within the directory
            for game_name in supported_games[directory]:

                # Get the full path to the games directory
                game_directory = current_directory.joinpath(
                    game_name, supported_games[directory][game_name])

                # Skip the game if it isn't installed
                if not game_directory.isdir():
                    continue

                # Yield the game and its path
                yield (game_name, game_directory)

# Get the dictionary of available games
available_games = {game: path for game, path in _get_available_games()}
