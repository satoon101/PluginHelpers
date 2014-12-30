# ../sp_linker.py

"""Links Source.Python's repository to servers."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Package Imports
from constants import SERVER_DIR
from constants import SOURCE_PYTHON_DIR
from constants import server_list
from functions import clear_screen
from functions import get_server
from functions import link_directory


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get the directories to link
_sp_directories = [
    x.namebase for x in SOURCE_PYTHON_DIR.dirs()
    if x.namebase not in ('addons', 'src', '.git')]

# Get the addons directories to link
_addons_directories = [
    x.namebase for x in SOURCE_PYTHON_DIR.joinpath(
        'addons', 'source-python').dirs() if x.namebase != 'bin'
]

# Get Source.Python's addons directory
_sp_addons = SOURCE_PYTHON_DIR.joinpath('addons', 'source-python')


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def link_server(server_name):
    """Link Source.Python's repository to the given server."""
    # Was an invalid server name given?
    if server_name not in server_list:
        print('Invalid server name "{0}".'.format(server_name))
        return

    # Get the server's path
    server_path = SERVER_DIR.joinpath(server_name, server_name)

    # Print a message about the linking
    print('Linking Source.Python to {0} server.\n'.format(server_name))

    # Loop through each directory to link
    for dir_name in _sp_directories:

        # Get the directory path
        directory = server_path.joinpath(dir_name)

        # Create the directory if it doesn't exist
        if not directory.isdir():
            directory.makedirs()

        # Get the source-python path
        sp_dir = directory.joinpath('source-python')

        # Does the source-python sub-directory already exist?
        if sp_dir.isdir():
            print(
                'Cannot link ../{0}/source-python/ directory.  '.format(
                    dir_name) + 'Directory already exists.\n')
            continue

        # Link the directory
        link_directory(
            SOURCE_PYTHON_DIR.joinpath(dir_name, 'source-python'), sp_dir)
        print('Successfully linked ../{0}/source-python/\n'.format(dir_name))

    # Get the server's addons directory
    server_addons = server_path.joinpath('addons', 'source-python')

    # Create the addons directory if it doesn't exist
    if not server_addons.isdir():
        server_addons.makedirs()

    # Loop through each directory to link
    for dir_name in _addons_directories:

        # Get the directory path
        directory = server_addons.joinpath(dir_name)

        # Does the directory already exist on the server?
        if directory.isdir():
            print('Cannot link ../addons/source-python/{0}/ directory.'.format(
                dir_name) + '  Directory already exists.\n')
            continue

        # Link the directory
        link_directory(_sp_addons.joinpath(dir_name), directory)
        print('Successfully linked ../addons/source-python/{0}/\n'.format(
            dir_name))

    # Get the bin directory
    bin_dir = server_addons.joinpath('bin')

    # Copy the bin directory if it doesn't exist
    if not bin_dir.isdir():
        _sp_addons.joinpath('bin').copytree(bin_dir)

    # Get the .vdf's path
    vdf = server_path.joinpath('addons', 'source-python.vdf')

    # Copy the .vdf if it needs copied
    if not vdf.isfile():
        SOURCE_PYTHON_DIR.joinpath('addons', 'source-python.vdf').copy(vdf)


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the server to link
    _server_name = get_server()

    # Was a valid server chosen?
    if _server_name is not None:

        # Clear the screen
        clear_screen()

        # Was ALL selected?
        if _server_name == 'ALL':

            # Loop through each server
            for _server_name in server_list:

                # Link the server
                link_server(_server_name)

        # Otherwise
        else:

            # Link the server
            link_server(_server_name)
