# ../plugin_creater/__main__.py

"""Used by Python to call plugin_creater from the command line."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Common Imports
from common.constants import plugin_list
from common.functions import clear_screen

# Package Imports
from plugin_creater import create_plugin


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
_boolean_values = {
    '1': True,
    'y': True,
    'yes': True,
    '2': False,
    'n': False,
    'no': False,
}

_directory_or_file = {
    '1': 'file',
    '2': 'directory',
    '3': None,
}


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def _get_plugin_name():
    """Return a new plugin name."""
    # Clear the screen
    clear_screen()

    # Ask for a valid plugin name
    name = input(
        'What is the name of the plugin that should be created?\n\n')

    # Is the plugin name invalid?
    if not name.replace('_', '').isalnum():

        # Try to get a new plugin name
        return _ask_retry(
            'Invalid characters used in plugin name "{0}".\n'.format(
                name) + 'Only alpha-numeric and underscores allowed.')

    # Does the plugin already exist?
    if name in plugin_list:

        # Try to get a new plugin name
        return _ask_retry(
            'Plugin name "{0}" already exists.'.format(name))

    # Return the plugin name
    return name


def _ask_retry(reason):
    """Ask if another plugin name should be given."""
    # Clear the screen
    clear_screen()

    # Get whether to retry or not
    value = input(
        reason + '\n\n' + 'Do you want to try again?\n\n' +
        '\t(1) Yes\n\t(2) No\n\n').lower()

    # Was the retry value invalid?
    if value not in _boolean_values:

        # Try again
        return _ask_retry(reason)

    # Was Yes selected?
    if _boolean_values[value]:

        # Try to get another plugin name
        return _get_plugin_name()

    # Simply return None to not get a plugin name
    return None


def _get_directory(name):
    """Return whether or not to create the given directory."""
    # Clear the screen
    clear_screen()

    # Get whether the directory should be added
    value = input(
        'Do you want to include a {0} directory?\n\n'.format(
            name) + '\t(1) Yes\n\t(2) No\n\n').lower()

    # Was the given value invalid?
    if value not in _boolean_values:

        # Try again
        return _get_directory(name)

    # Return the value
    return _boolean_values[value]


def _get_directory_or_file(name):
    """Return whether to create the given directory or file."""
    # Clear the screen
    clear_screen()

    # Get whether to add a directory, file, or neither
    value = input(
        'Do you want to include a {0} file, directory, or neither?\n\n'.format(
            name) + '\t(1) File\n\t(2) Directory\n\t(3) Neither\n\n')

    # Was the given value invalid?
    if value not in _directory_or_file:

        # Try again
        _get_directory_or_file(name)

    # Return the value
    return _directory_or_file[value]


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the plugin name to use
    plugin_name = _get_plugin_name()

    # Was a valid plugin name given?
    if plugin_name is not None:

        # Get the config value
        config = _get_directory('config')

        # Get the data value
        data = _get_directory_or_file('data')

        # Get the events value
        events = _get_directory('events')

        # Get the logs value
        logs = _get_directory('logs')

        # Get the sound value
        sound = _get_directory('sound')

        # Get the translations value
        translations = _get_directory_or_file('translations')

        # Call create_plugin with the options
        create_plugin(
            plugin_name, config, data, events, logs, sound, translations)
