# ../functions.py

"""Provides commonly used functions."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Contextlib
from contextlib import suppress
#   OS
from os import system

# Package Imports
from common.constants import CORE_BINARY
from common.constants import PLATFORM
from common.constants import SOURCE_BINARY
from common.constants import SOURCE_PYTHON_ADDONS_DIR
from common.constants import SOURCE_PYTHON_BUILDS_DIR
from common.constants import SOURCE_PYTHON_DIR
from common.constants import plugin_list
from common.constants import source_python_addons_directories
from common.constants import source_python_directories
from common.constants import supported_games


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def clear_screen():
    """Clear the screen."""
    system('cls' if PLATFORM == 'windows' else 'clear')


def get_plugin(suffix, allow_all=True):
    """Return a plugin by name to do something with."""
    # Clear the screen
    clear_screen()

    # Are there any plugins?
    if not plugin_list:
        print('There are no plugins to {0}.'.format(suffix))
        return None

    # Get the question to ask
    message = 'What plugin would you like to {0}?\n\n'.format(suffix)

    # Loop through each plugin
    for number, plugin in enumerate(plugin_list, 1):

        # Add the current plugin
        message += '\t({0}) {1}\n'.format(number, plugin)

    # Add ALL to the list if it needs to be
    if allow_all:
        message += '\t({0}) ALL\n'.format(len(plugin_list) + 1)

    # Ask which plugin to do something with
    value = input(message + '\n').strip()

    # Was a plugin name given?
    if value in plugin_list + ['ALL']:

        # Return the value
        return value

    # Was an integer given?
    with suppress(ValueError):

        # Typecast the value
        value = int(value)

        # Was the value a valid plugin choice?
        if value <= len(plugin_list):

            # Return the plugin by index
            return plugin_list[value - 1]

        # Was ALL's choice given?
        if value == len(plugin_list) + 1 and allow_all:

            # Return ALL
            return 'ALL'

    # If no valid choice was given, try again
    return get_plugin(suffix, allow_all)


def get_game():
    """Return a game to do something with."""
    # Clear the screen
    clear_screen()

    # Are there any games?
    if not supported_games:
        print('There are no games to link.')
        return None

    # Get the question to ask
    message = 'Which game/server would you like to link?\n\n'

    # Loop through each game
    for number, game in enumerate(supported_games, 1):

        # Add the current game
        message += '\t({0}) {1}\n'.format(number, game)

    # Add ALL to the list
    message += '\t({0}) ALL\n'.format(len(supported_games) + 1)

    # Ask which game to do something with
    value = input(message + '\n').strip()

    # Was a game name given?
    if value in list(supported_games) + ['ALL']:

        # Return the value
        return value

    # Was an integer given?
    with suppress(ValueError):

        # Typecast the value
        value = int(value)

        # Was the value a valid server choice?
        if value <= len(supported_games):

            # Return the game by index
            return list(supported_games)[value - 1]

        # Was ALL's choice given?
        if value == len(supported_games) + 1:

            # Return ALL
            return 'ALL'

    # If no valid choice was given, try again
    return get_game()


def link_directory(src, dest):
    """Create a symbolic link for the given source at the given destination."""
    # Is this a Windows OS?
    if PLATFORM == 'windows':

        # Link using Windows format
        system('mklink /d "{0}" "{1}"'.format(dest, src))

    # Is this a Linux OS?
    else:

        # Link using Linux format
        system('ln -s "{0}" "{1}"'.format(src, dest))


def link_file(src, dest):
    """Create a hard link for the given source at the given destination."""
    # Is this a Windows OS?
    if PLATFORM == 'windows':

        # Link using Windows format
        system('mklink "{0}" "{1}"'.format(dest, src))

    # Is this a Linux OS?
    else:

        # Link using Linux format
        system('ln -s "{0}" "{1}"'.format(src, dest))


def link_source_python(game_name):
    """Link Source.Python's repository to the given game/server."""
    # Get the path to the game/server
    path = supported_games[game_name]['directory']

    # Loop through each directory to link
    for dir_name in source_python_directories:

        # Get the directory path
        directory = path.joinpath(dir_name)

        # Create the directory if it doesn't exist
        if not directory.isdir():
            directory.makedirs()

        # Get the source-python path
        sp_dir = directory.joinpath('source-python')

        # Does the source-python sub-directory already exist?
        if sp_dir.isdir():
            print(
                'Cannot link ../{0}/source-python/ directory.  '.format(
                    dir_name) + 'Directory already exists.\n')
            continue

        # Link the directory
        link_directory(
            SOURCE_PYTHON_DIR.joinpath(dir_name, 'source-python'), sp_dir)
        print('Successfully linked ../{0}/source-python/\n'.format(dir_name))

    # Get the server's addons directory
    server_addons = path.joinpath('addons', 'source-python')

    # Create the addons directory if it doesn't exist
    if not server_addons.isdir():
        server_addons.makedirs()

    # Loop through each directory to link
    for dir_name in source_python_addons_directories:

        # Get the directory path
        directory = server_addons.joinpath(dir_name)

        # Does the directory already exist on the server?
        if directory.isdir():
            print('Cannot link ../addons/source-python/{0}/ directory.'.format(
                dir_name) + '  Directory already exists.\n')
            continue

        # Link the directory
        link_directory(SOURCE_PYTHON_ADDONS_DIR.joinpath(dir_name), directory)
        print('Successfully linked ../addons/source-python/{0}/\n'.format(
            dir_name))

    # Get the bin directory
    bin_dir = server_addons.joinpath('bin')

    # Copy the bin directory if it doesn't exist
    if not bin_dir.isdir():
        SOURCE_PYTHON_ADDONS_DIR.joinpath('bin').copytree(bin_dir)

    # Get the .vdf's path
    vdf = path.joinpath('addons', 'source-python.vdf')

    # Copy the .vdf if it needs copied
    if not vdf.isfile():
        SOURCE_PYTHON_DIR.joinpath('addons', 'source-python.vdf').copy(vdf)

    # Get the build directory for the game/server's branch
    build_dir = SOURCE_PYTHON_BUILDS_DIR.joinpath(
        supported_games[game_name]['branch'], 'Release')

    # If the build directory doesn't exist, create the build
    if not build_dir.isdir():
        warn('Build "{0}" does not exist.  Please create the build.'.format(
            branch))
        return

    # Link the files
    link_file(
        build_dir.joinpath(SOURCE_BINARY),
        path.joinpath('addons', SOURCE_BINARY))
    link_file(
        build_dir.joinpath(CORE_BINARY),
        path.joinpath('addons', 'source-python', 'bin', CORE_BINARY))