# ../plugin_checker/__init__.py

"""Used by Python to call plugin_cheker from the command line."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Common Imports
from common.constants import plugin_list
from common.functions import clear_screen
from common.functions import get_plugin

# Package Imports
from plugin_checker import check_plugin


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the plugin to check
    plugin_name = get_plugin('check')

    # Was a valid plugin chosen?
    if plugin_name is not None:

        # Clear the screen
        clear_screen()

        # Was ALL chosen?
        if plugin_name == 'ALL':

            # Loop through all plugins
            for plugin_name in plugin_list:

                # Check the current plugin
                check_plugin(plugin_name)

        # Was a valid plugin chosen?
        else:

            # Check the chosen plugin
            check_plugin(plugin_name)
