# ../plugin_checker.py

"""Checks plugins for standards issues."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   OS
from os import system

# Package Imports
from constants import PYTHON_EXE
from constants import START_DIR
from constants import config_obj
from constants import plugin_list
from functions import clear_screen
from functions import get_plugin


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def check_plugin(plugin_name):
    """Check the given plugin for standards issues."""
    # Was an invalid plugin name given?
    if plugin_name not in plugin_list:
        print('Invalid plugin name "{0}"'.format(plugin_name))
        return

    # Get the plugin's path
    plugin = START_DIR.joinpath(
        plugin_name, 'addons', 'source-python', 'plugins', plugin_name)

    # Check with pep8
    print_section('Checking "{0}" for PEP8 standards'.format(plugin_name))
    system('{0} -m pep8 --count --benchmark {1}'.format(PYTHON_EXE, plugin))

    # Check with pep257
    print_section(
        'Checking "{0}" for PEP257 standards'.format(plugin_name), True)
    system('{0} -m pep257 {1}'.format(PYTHON_EXE, plugin))

    # Check with pyflakes
    print_section('Checking "{0}" with PyFlakes'.format(plugin_name), True)
    system('{0} -m pyflakes {1}'.format(PYTHON_EXE, plugin))

    # Check with pylint
    print_section('Checking "{0}" with PyLint'.format(plugin_name), True)
    system(
        '{0} -m pylint --rcfile {1}/.pylintrc {2} '.format(
            PYTHON_EXE, START_DIR, plugin) +
        '--const-rgx="(([A-Z_][A-Z0-9_]*)|([a-z_][a-z0-9_]*)|(__.*__))$" ' +
        '--msg-template="{msg_id}:{line:3d},{column:2d}: {msg} ({symbol})"')


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
def print_section(message, separate=False):
    """Print the section header."""
    if separate:
        print('\n\n')
    print('=' * (len(message) + 1))
    print(message + ':')
    print('=' * (len(message) + 1) + '\n')


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the plugin to check
    _plugin_name = get_plugin('check')

    # Was a valid plugin chosen?
    if _plugin_name is not None:

        # Clear the screen
        clear_screen()

        # Was ALL chosen?
        if _plugin_name == 'ALL':

            # Loop through all plugins
            for _plugin_name in plugin_list:

                # Check the current plugin
                check_plugin(_plugin_name)

        # Was a valid plugin chosen?
        else:

            # Check the chosen plugin
            check_plugin(_plugin_name)
