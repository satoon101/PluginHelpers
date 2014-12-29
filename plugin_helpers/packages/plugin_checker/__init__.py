# ../plugin_checker/__init__.py

"""Checks plugins for standards issues."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   OS
from os import system

# Common Imports
from common.constants import START_DIR
from common.constants import config_obj
from common.constants import plugin_list


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def check_plugin(plugin_name):
    """Check the given plugin for standards issues."""
    # Was an invalid plugin name given?
    if plugin_name not in plugin_list:
        print('Invalid plugin name "{0}".  Plugin does not exist.'.format(
            plugin_name))
        return

    # Get the Python executable
    python = config_obj['PYTHONEXE']

    # Get the plugin's path
    plugin = START_DIR.joinpath(
        plugin_name, 'addons', 'source-python', 'plugins', plugin_name)

    # Check with pep8
    print_section('Checking "{0}" for PEP8 standards'.format(plugin_name))
    system('{0} -m pep8 --count --benchmark {1}'.format(python, plugin))

    # Check with pep257
    print_section(
        'Checking "{0}" for PEP257 standards'.format(plugin_name), True)
    system('{0} -m pep257 {1}'.format(python, plugin))

    # Check with pyflakes
    print_section('Checking "{0}" with PyFlakes'.format(plugin_name), True)
    system('{0} -m pyflakes {1}'.format(python, plugin))

    # Check with pylint
    print_section('Checking "{0}" with PyLint'.format(plugin_name), True)
    system(
        '{0} -m pylint --rcfile {1}/.pylintrc {2} '.format(
            python, START_DIR, plugin) +
        '--const-rgx="(([A-Z_][A-Z0-9_]*)|([a-z_][a-z0-9_]*)|(__.*__))$" ' +
        '--msg-template="{msg_id}:{line:3d},{column:2d}: {msg} ({symbol})"')


def print_section(message, separate=False):
    """Print the section header."""
    if separate:
        print('\n\n')
    print('=' * (len(message) + 1))
    print(message + ':')
    print('=' * (len(message) + 1) + '\n')
