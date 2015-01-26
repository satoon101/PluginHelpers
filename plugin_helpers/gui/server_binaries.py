# ../server_binaries.py

"""Copies Source.Python binaries to servers."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Package Imports
from common.constants import SERVER_DIR
from common.constants import SOURCE_PYTHON_BUILDS_DIR
from common.constants import server_list
from common.functions import copy_binaries
from common.functions import clear_screen
from common.functions import get_build
from common.functions import get_server
from common.functions import remove_release


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def copy_binaries_to_server(server_name):
    """Create a build for the given server."""
    # Was an invalid server name given
    if server_name not in server_list:
        print('Invalid server name "{0}".'.format(server_name))
        return

    # Get the build to use
    build = get_build(server_name)

    # Was no build found?
    if build is None:
        print('Unsupported server "{0}" for building.'.format(server_name))
        return

    # Print a message about the building
    print('Building Source.Python for {0} server.\n'.format(server_name))

    # Build for the server
    copy_binaries(SERVER_DIR.joinpath(server_name, server_name), build)


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

            # Loop through all builds with solutions
            for _build in SOURCE_PYTHON_BUILDS_DIR.dirs():

                # Remove the release directory
                remove_release(_build)

            # Loop through each server
            for _server_name in server_list:

                # Link the server
                copy_binaries_to_server(_server_name)

        # Otherwise
        else:

            # Remove the server's branch's Release directory
            remove_release(get_build(_server_name))

            # Link the server
            copy_binaries_to_server(_server_name)
