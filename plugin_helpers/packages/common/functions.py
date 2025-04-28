# ../common/functions.py

"""Provides commonly used functions."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from contextlib import suppress
from os import system
from warnings import warn

# Package
from common.constants import (
    CORE_BINARY,
    PLATFORM,
    SOURCE_BINARY,
    SOURCE_PYTHON_ADDONS_DIR,
    SOURCE_PYTHON_BUILDS_DIR,
    SOURCE_PYTHON_DIR,
    plugin_list,
    source_python_addons_directories,
    source_python_directories,
    supported_games,
)


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def clear_screen():
    """Clear the screen."""
    system("cls" if PLATFORM == "windows" else "clear")


def get_plugin(suffix, *, allow_all=True):
    """Return a plugin by name to do something with."""
    # Clear the screen
    clear_screen()

    # Are there any plugins?
    if not plugin_list:
        print(f"There are no plugins to {suffix}.")
        return None

    # Get the question to ask
    message = f"What plugin would you like to {suffix}?\n\n"

    # Loop through each plugin
    for number, plugin in enumerate(plugin_list, 1):

        # Add the current plugin
        message += f"\t({number}) {plugin}\n"

    # Add ALL to the list if it needs to be
    if allow_all:
        message += f"\t({len(plugin_list) + 1}) ALL\n"

    # Ask which plugin to do something with
    value = input(f"{message}\n").strip()

    # Was a plugin name given?
    if value in [*plugin_list, "ALL"]:

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
            return "ALL"

    # If no valid choice was given, try again
    return get_plugin(suffix, allow_all)


def get_game():
    """Return a game to do something with."""
    # Clear the screen
    clear_screen()

    # Are there any games?
    if not supported_games:
        print("There are no games to link.")
        return None

    # Get the question to ask
    message = "Which game/server would you like to link?\n\n"

    # Loop through each game
    for number, game in enumerate(supported_games, 1):

        # Add the current game
        message += f"\t({number}) {game}\n"

    # Add ALL to the list
    message += f"\t({len(supported_games) + 1}) ALL\n"

    # Ask which game to do something with
    value = input(f"{message}\n").strip()

    # Was a game name given?
    if value in [*supported_games, "ALL"]:

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
            return "ALL"

    # If no valid choice was given, try again
    return get_game()


def link_directory(src, dest):
    """Create a symbolic link for the given source at the given destination."""
    # Is this a Windows OS?
    if PLATFORM == "windows":

        # Link using Windows format
        system(f'mklink /d "{dest}" "{src}"')

    # Is this a Linux OS?
    else:

        # Link using Linux format
        system(f'ln -s "{src}" "{dest}"')


def link_file(src, dest):
    """Create a hard link for the given source at the given destination."""
    # Is this a Windows OS?
    if PLATFORM == "windows":

        # Link using Windows format
        system(f'mklink "{dest}" "{src}"')

    # Is this a Linux OS?
    else:

        # Link using Linux format
        system(f'ln -s "{src}" "{dest}"')


def link_source_python(game_name):
    """Link Source.Python's repository to the given game/server."""
    # Get the path to the game/server
    path = supported_games[game_name]["directory"]

    # Loop through each directory to link
    for dir_name in source_python_directories:

        # Get the directory path
        directory = path / dir_name

        # Create the directory if it doesn't exist
        if not directory.is_dir():
            directory.makedirs()

        # Get the source-python path
        sp_dir = directory / "source-python"

        # Does the source-python sub-directory already exist?
        if sp_dir.is_dir():
            print(
                f"Cannot link ../{dir_name}/source-python/ directory."
                f"  Directory already exists.\n",
            )
            continue

        # Link the directory
        link_directory(
            SOURCE_PYTHON_DIR / dir_name / "source-python", sp_dir,
        )
        print(f"Successfully linked ../{dir_name}/source-python/\n")

    # Get the server's addons directory
    server_addons = path / "addons" / "source-python"

    # Create the addons directory if it doesn't exist
    if not server_addons.is_dir():
        server_addons.makedirs()

    # Loop through each directory to link
    for dir_name in source_python_addons_directories:

        # Get the directory path
        directory = server_addons / dir_name

        # Does the directory already exist on the server?
        if directory.is_dir():
            print(
                f"Cannot link ../addons/source-python/{dir_name}/ "
                f"directory.  Directory already exists.\n",
            )
            continue

        # Link the directory
        link_directory(SOURCE_PYTHON_ADDONS_DIR / dir_name, directory)
        print(f"Successfully linked ../addons/source-python/{dir_name}/\n")

    # Get the bin directory
    bin_dir = server_addons / "bin"

    # Copy the bin directory if it doesn't exist
    if not bin_dir.is_dir():
        SOURCE_PYTHON_ADDONS_DIR.joinpath("bin").copytree(bin_dir)

    # Get the .vdf's path
    vdf = path / "addons" / "source-python.vdf"

    # Copy the .vdf if it needs copied
    if not vdf.is_file():
        SOURCE_PYTHON_DIR.joinpath("addons", "source-python.vdf").copy(vdf)

    # Get the build directory for the game/server's branch
    build_dir = SOURCE_PYTHON_BUILDS_DIR / supported_games[game_name]["branch"]

    # Add 'Release' to the directory if Windows
    if PLATFORM == "windows":
        build_dir = build_dir / "Release"

    # If the build directory doesn't exist, create the build
    if not build_dir.is_dir():
        warn(
            f'Build "{supported_games[game_name]["branch"]}" does not exist. '
            f'Please create the build.',
        )
        return

    # Link the files
    link_file(build_dir / SOURCE_BINARY, path / "addons" / SOURCE_BINARY)
    link_file(
        build_dir / CORE_BINARY,
        path / "addons" / "source-python" / "bin" / CORE_BINARY,
    )
