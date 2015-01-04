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
from constants import BINARY_EXTENSION
from constants import PLATFORM
from constants import SOURCE_PYTHON_ADDONS_DIR
from constants import SOURCE_PYTHON_BUILDS_DIR
from constants import SOURCE_PYTHON_DIR
from constants import available_games
from constants import plugin_list
from constants import server_list
from constants import source_python_addons_directories
from constants import source_python_directories
from constants import supported_builds


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


def get_server():
    """Return a server to do something with."""
    # Clear the screen
    clear_screen()

    # Are there any servers?
    if not server_list:
        print('There are no servers to link.')
        return None

    # Get the question to ask
    message = 'Which server would you like to link?\n\n'

    # Loop through each server
    for number, server in enumerate(server_list, 1):

        # Add the current server
        message += '\t({0}) {1}\n'.format(number, server)

    # Add ALL to the list
    message += '\t({0}) ALL\n'.format(len(server_list) + 1)

    # Ask which server to do something with
    value = input(message + '\n').strip()

    # Was a server name given?
    if value in server_list + ['ALL']:

        # Return the value
        return value

    # Was an integer given?
    with suppress(ValueError):

        # Typecast the value
        value = int(value)

        # Was the value a valid server choice?
        if value <= len(server_list):

            # Return the server by index
            return server_list[value - 1]

        # Was ALL's choice given?
        if value == len(server_list) + 1:

            # Return ALL
            return 'ALL'

    # If no valid choice was given, try again
    return get_server()


def get_game():
    """Return a game to do something with."""
    # Clear the screen
    clear_screen()

    # Are there any games?
    if not available_games:
        print('There are no games to link.')
        return None

    # Get the question to ask
    message = 'Which game would you like to link?\n\n'

    # Loop through each game
    for number, game in enumerate(sorted(available_games), 1):

        # Add the current game
        message += '\t({0}) {1}\n'.format(number, game)

    # Add ALL to the list
    message += '\t({0}) ALL\n'.format(len(available_games) + 1)

    # Ask which game to do something with
    value = input(message + '\n').strip()

    # Was a game name given?
    if value in list(available_games) + ['ALL']:

        # Return the value
        return value

    # Was an integer given?
    with suppress(ValueError):

        # Typecast the value
        value = int(value)

        # Was the value a valid server choice?
        if value <= len(available_games):

            # Return the game by index
            return sorted(available_games)[value - 1]

        # Was ALL's choice given?
        if value == len(available_games) + 1:

            # Return ALL
            return 'ALL'

    # If no valid choice was given, try again
    return get_game()


def link_directory(src, dest):
    """Create a symbolic link for the given source at the given destination."""
    # Is this a Windows OS?
    if PLATFORM == 'windows':

        # Link using Windows format
        system('mklink /J "{0}" "{1}"'.format(dest, src))

    # Is this a Linux OS?
    else:

        # Link using Linux format
        system('ln -s "{0}" "{1}"'.format(src, dest))


def link_file(src, dest):
    """Create a hard link for the given source at the given destination."""
    # Is this a Windows OS?
    if PLATFORM == 'windows':

        # Link using Windows format
        system('mklink /H "{0}" "{1}"'.format(dest, src))

    # Is this a Linux OS?
    else:

        # Link using Linux format
        system('ln "{0}" "{1}"'.format(src, dest))


def link_path(path):
    """Link Source.Python's repository to the given path."""
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


def get_build(name):
    """Return the build to use for the given name."""
    # Loop through all supported builds
    for build in supported_builds:

        # Does the current build support the given name?
        if name in supported_builds[build]:

            # Return the current build
            return build

    # If no build was found, return None
    return None


def remove_release(branch):
    """Remove the Release directory from the given branch."""
    # Was an invalid branch given?
    if branch is None:
        return

    # Get the release directory
    build_dir = SOURCE_PYTHON_BUILDS_DIR.joinpath(branch, 'Release')

    # Remove the Release directory
    if build_dir.isdir():
        for file in build_dir.files():
            file.remove()
        build_dir.removedirs()


def compile_build(branch):
    """Compile the given branch."""
    # Is this a Windows OS?
    if PLATFORM == 'windows':

        # Create a build in Windows
        system('call plugin_helpers/windows/compile_build {0}'.format(branch))

    # Is this a Linux OS?
    else:

        # Create a build in Linux
        system('sh plugin_helpers/linux/compile_build {0}'.format(branch))


def copy_binaries(path, branch):
    """Create a build for the given branch and copy to the given path."""
    # Get the build directory from the branch
    build_dir = SOURCE_PYTHON_BUILDS_DIR.joinpath(branch, 'Release')

    # If the build directory doesn't exist, create the build
    if not build_dir.isdir():
        compile_build(branch)

    # Copy the files
    build_dir.joinpath('source-python.{0}'.format(BINARY_EXTENSION)).copy(
        path.joinpath('addons', 'source-python.{0}'.format(BINARY_EXTENSION)))
    build_dir.joinpath('core.{0}'.format(BINARY_EXTENSION)).copy(
        path.joinpath('addons', 'source-python', 'bin', 'core.{0}'.format(
            BINARY_EXTENSION)))
