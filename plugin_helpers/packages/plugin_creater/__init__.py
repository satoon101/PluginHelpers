# ../plugin_creater/__init__.py

"""Creates a plugin with its base directories and files."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Common Imports
from common.constants import START_DIR
from common.constants import config_obj


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def create_plugin(
        plugin_name, config=False, data=None, events=False,
        logs=False, sound=False, translations=None):
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
        print('Please delete config.ini and re-run config.bat.')
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
    if config:

        # Create the cfg directory
        _create_directory(
            plugin_base_path, 'cfg', 'source-python',
            plugin_name, filename='readme.md')

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
    if events:

        # Create the events directory
        _create_directory(
            plugin_base_path, 'resource', 'source-python',
            'events', plugin_name, filename='readme.md')

    # Should a logs directory be created?
    if logs:

        # Create the logs directory
        _create_directory(
            plugin_base_path, 'logs', 'source-python',
            plugin_name, filename='readme.md')

    # Should a sound directory be created?
    if sound:

        # Create the sound directory
        _create_directory(
            plugin_base_path, 'sound', 'source-python', plugin_name)

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
