# ../common/constants.py

"""Provides commonly used constants."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Collections
from collections import OrderedDict
#   Platform
from platform import system
#   Warnings
from warnings import warn

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

# Store the binary names
SOURCE_BINARY = 'source-python.{0}'.format(
    'dll' if PLATFORM == 'windows' else 'so')
CORE_BINARY = 'core.{0}'.format('dll' if PLATFORM == 'windows' else 'so')

# Store the main directory
START_DIR = Path(__file__).parent.parent.parent.parent

# Store the premade files location
PREMADE_FILES_DIR = START_DIR.joinpath('plugin_helpers', 'files')

# Get the configuration
config_obj = ConfigObj(START_DIR.joinpath('config.ini'))

# Store the author value
AUTHOR = config_obj['AUTHOR']

# Store the Source.Python repository directory
SOURCE_PYTHON_DIR = Path(config_obj['SOURCE_PYTHON_DIRECTORY'])

# Get Source.Python's addons directory
SOURCE_PYTHON_ADDONS_DIR = SOURCE_PYTHON_DIR.joinpath(
    'addons', 'source-python')

# Get Source.Python's build directory
SOURCE_PYTHON_BUILDS_DIR = SOURCE_PYTHON_DIR.joinpath('src', 'Builds')

# Get the directories to link
source_python_directories = {
    x.namebase for x in SOURCE_PYTHON_DIR.dirs()
    if x.namebase not in ('addons', 'src', '.git')}

# Get the addons directories to link
source_python_addons_directories = {
    x.namebase for x in SOURCE_PYTHON_DIR.joinpath(
        'addons', 'source-python').dirs() if x.namebase != 'bin'}

_support = ConfigObj(START_DIR.joinpath(
    'plugin_helpers', 'tools', 'support.ini'))

supported_games = OrderedDict()

_check_file = 'srcds.exe' if PLATFORM == 'windows' else 'srcds_run'

for _directory in config_obj['SERVER_DIRECTORIES'].split(';'):
    _path = Path(_directory)
    for _check_directory in _path.dirs():
        if not _check_directory.joinpath(_check_file).isfile():
            continue
        for _game in _support['servers']:
            _game_dir = _check_directory.joinpath(
                _support['servers'][_game]['folder'])
            if not _game_dir.isdir():
                continue
            if _game in supported_games:
                warn(
                    '{0} already assigned to {1}.  New path found: {2}'.format(
                        _game, supported_games[_game], _game_dir))
                continue
            supported_games[_game] = {
                'directory': _game_dir,
                'branch': _support['servers'][_game]['branch']}

for _directory in config_obj['STEAM_DIRECTORIES'].split(';'):
    _path = Path(_directory).joinpath('SteamApps')
    for _game_type in ('common', 'sourcemods'):
        for _game in _support[_game_type]:
            _game_dir = _path.joinpath(
                _game_type, _game, _support['common'][_game]['folder'])
            if not _game_dir.isdir():
                continue
            if _game in supported_games:
                warn(
                    '{0} already assigned to {1}.  New path found: {2}'.format(
                        _game, supported_games[_game], _game_dir))
                continue
            supported_games[_game] = {
                'directory': _game_dir,
                'branch': _support[_game_type][_game]['branch']}

# Store the Release directory
RELEASE_DIR = Path(config_obj['RELEASE_DIRECTORY'])

# Store the Python executable path
PYTHON_EXE = config_obj['PYTHON_EXECUTABLE']

# Get a list of all plugins
plugin_list = [
    x.namebase for x in START_DIR.dirs()
    if x.namebase not in ('plugin_helpers', '.git', '__pycache__')]
