# ../sp_linker/__main__.py

"""Used by Python to call sp_linker from the command line."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Common Imports
from common.constants import server_list
from common.functions import clear_screen
from common.functions import get_server

# Package Imports
from sp_linker import link_server


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the server to link
    server_name = get_server()

    # Was a valid server chosen?
    if server_name is not None:

        # Clear the screen
        clear_screen()

        # Was ALL selected?
        if server_name == 'ALL':

            # Loop through each server
            for server_name in server_list:

                # Link the server
                link_server(server_name)

        # Otherwise
        else:

            # Link the server
            link_server(server_name)
