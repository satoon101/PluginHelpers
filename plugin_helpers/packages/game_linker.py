# ../game_linker.py

"""Links Source.Python's repository to games."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Package Imports
from constants import available_games
from functions import clear_screen
from functions import get_game
from functions import link_path


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def link_game(game_name):
    """Link Source.Python's repository to the given game."""
    # Was an invalid game name given?
    if game_name not in available_games:
        print('Invalid game name "{0}".'.format(game_name))
        return

    # Print a message about the linking
    print('Linking Source.Python to {0} game.\n'.format(game_name))

    # Link Source.Python to the game
    link_path(available_games[game_name])


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

            # Loop through each game
            for _game_name in available_games:

                # Link the game
                link_game(_game_name)

        # Otherwise
        else:

            # Link the game
            link_game(_game_name)
