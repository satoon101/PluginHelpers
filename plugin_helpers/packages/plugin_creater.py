# ../plugin_creater.py

"""Creates a plugin with its base directories and files."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Package Imports
from common.constants import AUTHOR
from common.constants import PREMADE_FILES_DIR
from common.constants import START_DIR
from common.constants import config_obj
from common.constants import plugin_list
from common.functions import clear_screen


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
# >> MAIN FUNCTION
# =============================================================================
def create_plugin(plugin_name, **options):
    """Verify the plugin name and create its base directories/files."""
    # Was no plugin name provided?
    if plugin_name is None:
        print('No plugin name provided.')
        return

    # Is the given plugin name valid?
    if not plugin_name.replace('_', '').isalnum():
        print('Invalid plugin name.')
        print(
            'Plugin name must only contain ' +
            'alpha-numeric values and underscores.')
        return

    # Get the path to create the plugin at
    plugin_base_path = START_DIR.joinpath(plugin_name)

    # Has the plugin already been created?
    if plugin_base_path.isdir():
        print('Plugin already exists.')
        return

    # Get the plugin's directory
    plugin_path = plugin_base_path.joinpath(
        'addons', 'source-python', 'plugins', plugin_name)

    # Create the plugin's directory
    plugin_path.makedirs()

    _copy_file(plugin_path.joinpath('__init__.py'))

    _copy_file(plugin_path.joinpath('info.py'))

    _copy_file(plugin_path.joinpath(plugin_name + '.py'))

    # Should a cfg directory be created?
    if options.get('config', False):

        # Create the cfg directory
        _create_directory(
            plugin_base_path, 'cfg', 'source-python',
            plugin_name, filename='readme.md')

    # Get the data option value
    data = options.get('data', None)

    # Should a data file be created?
    if data == 'file':

        # Create the data file
        _create_directory(
            plugin_base_path, 'addons', 'source-python',
            'data', 'plugins', filename=plugin_name + '.ini')

    # Should a data directory be created?
    elif data == 'directory':

        # Create the data directory
        _create_directory(
            plugin_base_path, 'addons', 'source-python',
            'data', 'plugins', plugin_name)

    # Should a docs directory be created?
    if options.get('docs', False):

        # Create the docs directory
        _create_directory(
            plugin_base_path, 'addons', 'source-python',
            'docs', 'plugins', plugin_name, filename='readme.md')

    # Should a events directory be created?
    if options.get('events', False):

        # Create the events directory
        _create_directory(
            plugin_base_path, 'resource', 'source-python',
            'events', plugin_name, filename='readme.md')

    # Should a logs directory be created?
    if options.get('logs', False):

        # Create the logs directory
        _create_directory(
            plugin_base_path, 'logs', 'source-python',
            plugin_name, filename='readme.md')

    # Should a sound directory be created?
    if options.get('sound', False):

        # Create the sound directory
        _create_directory(
            plugin_base_path, 'sound', 'source-python', plugin_name)

    # Get the translations option value
    translations = options.get('translations', None)

    # Should a translations file be created?
    if translations == 'file':

        # Create the translations file
        _create_directory(
            plugin_base_path, 'resource', 'source-python',
            'translations', filename=plugin_name + '.ini')

    # Should a translations directory be created?
    elif translations == 'directory':

        # Create the translations directory
        _create_directory(
            plugin_base_path, 'resource', 'source-python',
            'translations', plugin_name)

    # Loop through all premade files
    for file in PREMADE_FILES_DIR.files():

        # Skip Python files
        if file.ext == '.py':
            continue

        # Copy the file to the plugin's base directory
        PREMADE_FILES_DIR.joinpath(file.namebase).copy(
            plugin_base_path.joinpath(file.namebase))


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
def _copy_file(filepath):
    """"""
    if PREMADE_FILES_DIR.joinpath(filepath.name).isfile():

        PREMADE_FILES_DIR.joinpath(filepath.name).copy(filepath)

    else:

        PREMADE_FILES_DIR.joinpath('plugin.py').copy(filepath)

    with filepath.open() as open_file:

        file_contents = open_file.read()

    plugin_name = filepath.parent.namebase

    plugin_title = plugin_name.replace('_', ' ').title()

    file_contents = file_contents.replace('$plugin_name', plugin_name).replace(
        '$plugin_title', plugin_title).replace('$author', AUTHOR)

    with filepath.open('w') as open_file:

        open_file.write(file_contents)


def _create_directory(base_path, *args, filename=None):
    """Create the directory using the given arguments."""
    # Get the path to create
    current_path = base_path.joinpath(*args)

    # Create the directory
    current_path.makedirs()

    # Was a filename given?
    if filename is not None:

        # Create the file
        current_path.joinpath(filename).touch()


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
    _plugin_name = _get_plugin_name()

    # Was a valid plugin name given?
    if _plugin_name is not None:

        # Get the config value
        _config = _get_directory('config')

        # Get the data value
        _data = _get_directory_or_file('data')

        # Get the docs value
        _docs = _get_directory('docs')

        # Get the events value
        _events = _get_directory('events')

        # Get the logs value
        _logs = _get_directory('logs')

        # Get the sound value
        _sound = _get_directory('sound')

        # Get the translations value
        _translations = _get_directory_or_file('translations')

        # Call create_plugin with the options
        create_plugin(
            _plugin_name, config=_config, data=_data, docs=_docs,
            events=_events, logs=_logs, sound=_sound,
            translations=_translations)
