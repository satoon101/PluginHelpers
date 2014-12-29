# ../sp_linker/__init__.py

"""Links Source.Python's repository to servers."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Common Imports
from common.constants import SERVER_DIR
from common.constants import SOURCE_PYTHON_DIR
from common.constants import server_list
from common.functions import link_directory


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get the directories to link
_sp_directories = [
    x.namebase for x in SOURCE_PYTHON_DIR.dirs()
    if x.namebase not in ('src', '.git')]


# =============================================================================
# >> FUNCTIONS
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
    print('Linking Source.Python to {0} server.'.format(server_name))

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
                    dir_name) + 'Directory already exists.')
            continue

        # Link the directory
        link_directory(
            SOURCE_PYTHON_DIR.joinpath(dir_name, 'source-python'), sp_dir)

    # Get the .vdf's path
    vdf = server_path.joinpath('addons', 'source-python.vdf')

    # Copy the .vdf if it needs copied
    if not vdf.isfile():
        SOURCE_PYTHON_DIR.joinpath('addons', 'source-python.vdf').copy(vdf)
