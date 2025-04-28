# ../plugin_checker.py

"""Checks plugins for standards issues."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from os import system

# Package
from common.constants import START_DIR, plugin_list
from common.functions import clear_screen, get_plugin


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def check_plugin(plugin_name):
    """Check the given plugin for standards issues."""
    # Was an invalid plugin name given?
    if plugin_name not in plugin_list:
        print(f'Invalid plugin name "{plugin_name}"')
        return

    # Get the plugin's path
    plugin = START_DIR.joinpath(
        plugin_name,
        "addons",
        "source-python",
        "plugins",
        plugin_name,
    )

    system(f"ruff check")


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == "__main__":

    # Get the plugin to check
    _plugin_name = get_plugin("check")
    if _plugin_name is None:
        return

    clear_screen()
    if _plugin_name == "ALL":
        for _plugin_name in plugin_list:
            print(f'Checking plugin "{plugin_name}"')
            check_plugin(_plugin_name)

    else:
        check_plugin(_plugin_name)
