# ../game_binaries.py

"""Copies Source.Python binaries to games."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Package Imports
from constants import SOURCE_PYTHON_BUILDS_DIR
from constants import available_games
from constants import game_directories
from functions import copy_binaries
from functions import clear_screen
from functions import get_build
from functions import get_game
from functions import remove_release


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def copy_binaries_to_game(game_name):
    """Create a build for the given game."""
    # Was an invalid game name given?
    if game_name not in available_games:
        print('Invalid game name "{0}".'.format(game_name))
        return

    # Get the build to use
    build = get_build(game_directories[game_name] or game_name)

    # Was no build found?
    if build is None:
        print('Unsupported game "{0}" for building.'.format(game_name))
        return

    # Print a message about the building
    print('Building Source.Python for {0} game.\n'.format(game_name))

    # Build for the game
    copy_binaries(available_games[game_name], build)


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the game to link
    _game_name = get_game()

    # Was a valid game chosen?
    if _game_name is not None:

        # Clear the screen
        clear_screen()

        # Was ALL selected?
        if _game_name == 'ALL':

            # Loop through all builds with solutions
            for _build in SOURCE_PYTHON_BUILDS_DIR.dirs():

                # Remove the release directory
                remove_release(_build)

            # Loop through each game
            for _game_name in available_games:

                # Copy the binaries to the game
                copy_binaries_to_game(_game_name)

        # Otherwise
        else:

            # Remove the game's branch's Release directory
            remove_release(
                get_build(game_directories[_game_name] or _game_name))

            # Copy the binaries to the game
            copy_binaries_to_game(_game_name)
