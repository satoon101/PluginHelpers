# ../plugin_creater.py

"""Creates a plugin with its base directories and files."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Package Imports
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

    # Use try/except to retrieve the author name
    try:

        # Get the author name to use
        author = config_obj['AUTHOR']

        # Get the repo type to use
        repo_type = config_obj['REPOTYPE']

    # Was one of the keys not found in the config.ini?
    except KeyError as key:
        print('No "{0}" found in config.ini.'.format(key))
        print('Please delete config.ini and re-run setup.bat.')
        return

    # Get the base path for the plugin's directory
    plugin_home_path = plugin_base_path.joinpath(
        'addons', 'source-python', 'plugins')

    # Get the plugin's directory
    plugin_path = plugin_home_path.joinpath(plugin_name)

    # Create the plugin's directory
    plugin_path.makedirs()

    # Create the __init__.py
    with plugin_path.joinpath('__init__.py').open('w') as open_file:
        _write_top_lines(open_file, plugin_home_path)

    # Create the <plugin_name>.py
    with plugin_path.joinpath(plugin_name + '.py').open('w') as open_file:
        _write_top_lines(open_file, plugin_home_path)

    # Create the info.py
    with plugin_path.joinpath('info.py').open('w') as open_file:
        _write_top_lines(open_file, plugin_home_path)
        _write_info(open_file, plugin_name, author)

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

    # Create the repo specific files
    _create_repo(repo_type, plugin_base_path)


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
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


def _create_repo(repo_type, base_path):
    """Create repo specific ignore/attributes files."""
    # Should .gitignore and .gitattributes be created?
    if repo_type == 'git':

        # Create the .gitignore and .gitattributes
        with base_path.joinpath('.gitignore').open('w') as open_file:
            open_file.write('__pycache__/\n')
        with base_path.joinpath('.gitattributes').open('w') as open_file:
            open_file.write(
                '# Set default behaviour, in case users ' +
                "don't have core.autocrlf set.\n")
            open_file.write(
                '# Adding * text=auto causes Git to autodetect ' +
                'text files and normalise their\n')
            open_file.write(
                '# line endings to LF when they are ' +
                'checked into your repository.\n')
            open_file.write('* text=auto\n')

    # Should .hgignore be created?
    elif repo_type == 'hg':

        # Create the .hgignore
        with base_path.joinpath('.hgignore').open('w') as open_file:
            open_file.write('__pycache__/\n')


def _write_top_lines(open_file, path):
    """Write the header of the file."""
    open_file.write('# ..{0}\n\n"""."""\n\n'.format(
        open_file.name.split(path, 1)[1].replace('\\', '/')))


def _write_info(open_file, plugin_name, author):
    """Write the info.py file."""
    # Write the import section header
    separator = '# {0}\n'.format('=' * 77)
    open_file.write(separator)
    open_file.write('# >> IMPORTS\n')
    open_file.write(separator)

    # Write the imports
    open_file.write('# Source.Python Imports\n')
    open_file.write('#   Cvars\n')
    open_file.write('from cvars.public import PublicConVar\n')
    open_file.write('#   Plugins\n')
    open_file.write('from plugins.info import PluginInfo\n\n\n')

    # Write the plugin info section header
    open_file.write(separator)
    open_file.write('# >> PLUGIN INFO\n')
    open_file.write(separator)

    # Write the plugin info
    open_file.write('info = PluginInfo()\n')
    open_file.write("info.name = '{0}'\n".format(
        plugin_name.replace('_', ' ').title()))
    open_file.write("info.author = '{0}'\n".format(author))
    open_file.write("info.version = '1.0'\n")
    open_file.write("info.basename = '{0}'\n".format(plugin_name))
    open_file.write("info.variable = info.basename + '_version'\n")
    open_file.write("info.url = ''\n")
    open_file.write('info.convar = PublicConVar(\n')
    open_file.write(
        "    info.variable, info.version, 0, info.name + ' Version')\n")


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
            _plugin_name, config=_config, data=_data, events=_events,
            logs=_logs, sound=_sound, translations=_translations)
