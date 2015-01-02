# ../server_linker.py

"""Links Source.Python's repository to servers."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Package Imports
from constants import SERVER_DIR
from constants import server_list
from functions import clear_screen
from functions import get_server
from functions import link_path


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def link_server(server_name):
    """Link Source.Python's repository to the given server."""
    # Was an invalid server name given?
    if server_name not in server_list:
        print('Invalid server name "{0}".'.format(server_name))
        return

    # Print a message about the linking
    print('Linking Source.Python to {0} server.\n'.format(server_name))

    # Link Source.Python to the server
    link_path(SERVER_DIR.joinpath(server_name, server_name))


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the server to link
    _server_name = get_server()

    # Was a valid server chosen?
    if _server_name is not None:

        # Clear the screen
        clear_screen()

        # Was ALL selected?
        if _server_name == 'ALL':

            # Loop through each server
            for _server_name in server_list:

                # Link the server
                link_server(_server_name)

        # Otherwise
        else:

            # Link the server
            link_server(_server_name)
