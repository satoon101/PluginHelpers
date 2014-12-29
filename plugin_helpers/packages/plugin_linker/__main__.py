# ../plugin_linker/__main__.py

"""Used by Python to call plugin_linker from the command line."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Common Imports
from common.constants import plugin_list
from common.constants import server_list
from common.functions import clear_screen
from common.functions import get_plugin
from common.functions import get_server

# Package Imports
from plugin_linker import link_plugin


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def _link_server(server, plugin):
    """Link the server with the plugin."""
    # Was ALL selected for the plugin?
    if plugin == 'ALL':

        # Loop through each plugin
        for plugin in plugin_list:

            # Link the plugin
            link_plugin(server, plugin)

    # Otherwise
    else:

        # Link the plugin
        link_plugin(server, plugin)


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the plugin to link
    plugin_name = get_plugin('link')

    # Was a valid plugin chosen?
    if plugin_name is not None:

        # Clear the screen
        clear_screen()

        # Get the server to link
        server_name = get_server()

        # Was a valid server chosen?
        if server_name is not None:

            # Clear the screen
            clear_screen()

            # Was ALL selected for the server?
            if server_name == 'ALL':

                # Loop through each server
                for server_name in server_list:

                    # Link the server to the plugin
                    _link_server(server_name, plugin_name)

            # Otherwise
            else:

                # Link the server to the plugin
                _link_server(server_name, plugin_name)
