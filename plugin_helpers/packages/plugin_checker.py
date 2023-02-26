# ../plugin_checker.py

"""Checks plugins for standards issues."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from os import system

# Package
from common.constants import PYTHON_EXE
from common.constants import START_DIR
from common.constants import plugin_list
from common.functions import clear_screen
from common.functions import get_plugin


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
        'addons',
        'source-python',
        'plugins',
        plugin_name,
    )

    # Check with pep8
    print_section(f'Checking "{plugin_name}" for coding standards')
    system(f'{PYTHON_EXE} -m pycodestyle --count --benchmark {plugin}')

    # Check with pep257
    print_section(
        f'Checking "{plugin_name}" for docstring standards',
        True,
    )
    system(f'{PYTHON_EXE} -m pydocstyle {plugin}')

    # Check with pyflakes
    print_section(
        f'Checking "{plugin_name}" with PyFlakes',
        True,
    )
    system(f'{PYTHON_EXE} -m pyflakes {plugin}')

    # Check with pylint
    print_section(
        f'Checking "{plugin_name}" with PyLint',
        True,
    )
    system(
        f'{PYTHON_EXE} -m pylint '
        f'--rcfile {START_DIR / plugin_name}/.pylintrc {plugin}'
    )


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
