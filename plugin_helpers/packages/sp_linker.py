# ../sp_linker.py

"""Links Source.Python's repository to games/servers."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Package
from common.constants import supported_games
from common.functions import clear_screen
from common.functions import get_game
from common.functions import link_source_python


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def link_game(game_name):
    """Link Source.Python's repository to the given game/server."""
    # Was an invalid game name given?
    if game_name not in supported_games:
        print('Invalid game name "{game_name}".'.format(game_name=game_name))
        return

    # Print a message about the linking
    print(
        'Linking Source.Python to {game_name}.\n'.format(game_name=game_name)
    )

    # Link Source.Python to the game
    link_source_python(game_name)


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
            for _game_name in supported_games:

                # Link the game
                link_game(_game_name)

        # Otherwise
        else:

            # Link the game
            link_game(_game_name)
