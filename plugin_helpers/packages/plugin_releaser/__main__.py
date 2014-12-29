# ../plugin_releaser/__main__.py

"""Used by Python to call plugin_releaser from the command line."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Common Imports
from common.functions import clear_screen
from common.functions import get_plugin

# Package Imports
from plugin_releaser import create_release


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the plugin to check
    plugin_name = get_plugin('release', False)

    # Was a valid plugin chosen?
    if plugin_name is not None:

        # Clear the screen
        clear_screen()

        # Create a release for the chosen plugin
        create_release(plugin_name)
