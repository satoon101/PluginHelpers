# ../plugin_releaser/__init__.py

"""Creates a release for a plugin with its current version number."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Contextlib
from contextlib import suppress
#   Zipfile
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile

# Site-Package Imports
#   Configobj
from configobj import ConfigObj
from configobj import ConfigObjError
#   Path
from path import Path

# Package Imports
from plugin_releaser.paths import CONFIG_FILE
from plugin_releaser.paths import STARTDIR
from plugin_releaser.paths import allowed_filetypes
from plugin_releaser.paths import exception_filetypes
from plugin_releaser.paths import other_filetypes


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def create_release(plugin_name=None):
    """Verify the plugin name and create the current release."""
    # Was no plugin name provided?
    if plugin_name is None:
        print('No plugin name provided.')
        return

    # Does the config file exist?
    if not CONFIG_FILE.isfile():
        print('config.ini file not found, please run config.bat.')
        return

    # Use try/except to retrieve the release directory
    try:

        # Get the release directory
        release_path = ConfigObj(CONFIG_FILE)['RELEASEDIR']

    # Was 'RELEASEDIR' not found in the config.ini?
    except KeyError:
        print('No release path found in config.ini.')
        print('Please delete config.ini and re-run config.bat.')
        return

    # Was there an error in the config.ini?
    except ConfigObjError:
        print('config.ini has errors.')
        print('Please delete config.ini and re-run config.bat.')
        return

    # Get the plugin's base path
    plugin_path = STARTDIR.joinpath(plugin_name)

    # Does the plugin not exist?
    if not plugin_path.isdir():
        print('Plugin "{0}" not found.'.format(plugin_name))
        return

    # Get the plugin's current version
    version = get_version(plugin_path.joinpath(
        'addons', 'source-python', 'plugins', plugin_name))

    # Was no version information found?
    if version is None:
        print('No version found.')
        return

    # Get the directory to save the release in
    save_path = Path(release_path).joinpath(plugin_name)

    # Create the directory if it doesn't exist
    if not save_path.isdir():
        save_path.makedirs()

    # Get the full path to the release zip file
    zip_path = save_path.joinpath(
        '{0} - v{1}.zip'.format(plugin_name, version))

    # Does the release already exist?
    if zip_path.isfile():
        print('Release already exists for current version.')
        return

    # Create the zip file
    with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zip_file:

        # Loop through all allowed directories
        for allowed_path in allowed_filetypes:

            # Get the full path to the directory
            check_path = plugin_path.joinpath(*allowed_path.split('/'))

            # Does the directory exist?
            if not check_path.isdir():
                continue

            # Loop through all files with the plugin's name
            for file in find_files(check_path.files('{0}.*'.format(
                    plugin_name)), allowed_path, allowed_filetypes):

                # Add the file to the zip
                add_file(zip_file, file, plugin_path)

            # Loop through all files within the plugin's directory
            for file in find_files(check_path.joinpath(
                    plugin_name).walkfiles(), allowed_path, allowed_filetypes):

                # Add the file to the zip
                add_file(zip_file, file, plugin_path)

        # Loop through all other allowed directories
        for allowed_path in other_filetypes:

            # Get the full path to the directory
            check_path = plugin_path.joinpath(*allowed_path.split('/'))

            # Does the directory exist?
            if not check_path.isdir():
                continue

            # Loop through all files in the directory
            for file in find_files(
                    check_path.walkfiles(), allowed_path, other_filetypes):

                # Add the file to the zip
                add_file(zip_file, file, plugin_path)

    # Print a message that everything was successful
    print('Successfully created {0} version {1} release:'.format(
        plugin_name, version))
    print('\t"{0}"'.format(zip_path))


def get_version(plugin_path):
    """Return the version for the plugin."""
    # Loop through all Python files for the plugin
    for file in plugin_path.files('*.py'):

        # Open the file
        with file.open() as open_file:

            # Get the contents of the file
            contents = open_file.read()

            # Is the version information not contained in the current file?
            if 'info.version = ' not in contents:
                continue

            # Return the version
            return contents.split(
                'info.version = ', 1)[1].splitlines()[0][1:~0]

    # If no version information was found, simply return None
    return None


def find_files(generator, allowed_path, allowed_dictionary):
    """Yield files that should be added to the zip."""
    # Suppress FileNotFoundError in case the
    #    plugin specific directory does not exist.
    with suppress(FileNotFoundError):

        # Loop through the files from the given generator
        for file in generator:

            # Is the current file not allowed?
            if not file.ext[1:] in allowed_dictionary[allowed_path]:
                continue

            # Does the given directory have exceptions?
            if allowed_path in exception_filetypes:

                # Loop through the directory's exceptions
                for exception in exception_filetypes[allowed_path]:

                    # Is this file not allowed?
                    if exception in file.name:
                        break

                # Is the file not an exception?
                else:
                    yield file

            # Is the file allowed?
            else:
                yield file


def add_file(zip_file, file, plugin_path):
    """Add the given file and all parent directories to the zip."""
    # Write the file to the zip
    zip_file.write(file, file.replace(plugin_path, ''))

    # Get the file's parent directory
    parent = file.parent

    # Get all parent directories to add to the zip
    while plugin_path != parent:

        # Is the current directory not yet included in the zip?
        current = parent.replace(plugin_path, '')[1:].replace('\\', '/') + '/'
        if current not in zip_file.namelist():

            # Add the parent directory to the zip
            zip_file.write(parent, current)

        # Get the parent's parent
        parent = parent.parent
