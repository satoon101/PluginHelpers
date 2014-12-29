# ../plugin_linker/__init__.py

"""Links plugins to servers."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Common Imports
from common.constants import SOURCE_PYTHON_DIR
from common.constants import START_DIR
from common.constants import plugin_list
from common.functions import link_directory
from common.functions import link_file


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def link_plugin(plugin_name):
    """Link the given plugin name to Source.Python's repository."""
    # Was an invalid plugin name given?
    if plugin_name not in plugin_list:
        print('Invalid plugin name "{0}"'.format(plugin_name))
        return

    # Get the plugin's path
    plugin_path = START_DIR.joinpath(plugin_name)

    # Link the main directory
    _link_directory(
        plugin_path, 'addons', 'source-python', 'plugins', plugin_name)

    # Link the data directory
    _link_directory(
        plugin_path, 'addons', 'source-python', 'data', 'plugins', plugin_name)

    # Link the data file
    _link_file(
        plugin_path, 'addons', 'source-python', 'data', 'plugins', plugin_name)

    # Link the cfg directory
    _link_directory(plugin_path, 'cfg', 'source-python', plugin_name)

    # Link the logs directory
    _link_directory(plugin_path, 'logs', 'source-python', plugin_name)

    # Link the events directory
    _link_directory(
        plugin_path, 'resource', 'source-python', 'events', plugin_name)

    # Link the translations directory
    _link_directory(
        plugin_path, 'resource', 'source-python', 'translations', plugin_name)

    # Link the translations file
    _link_file(
        plugin_path, 'resource', 'source-python', 'translations', plugin_name)

    # Link the sound directory
    _link_directory(plugin_path, 'sound', 'source-python', plugin_name)


def _link_directory(plugin_path, *args):
    """Link the directory using the given arguments."""
    # Get the path within the plugin
    src = plugin_path.joinpath(*args)

    # Does the path not exist?
    if not src.isdir():
        return

    # Get the path within the Source.Python repository
    dest = SOURCE_PYTHON_DIR.joinpath(*args)

    # Does the destination not exist?
    if not dest.isdir():

        # Link the directory
        link_directory(src, dest)


def _link_file(plugin_path, *args):
    """Link the file using the given arguments."""
    # Append .ini to the last argument
    args = list(args)
    args[~0] += '.ini'

    # Get the path within the plugin
    src = plugin_path.joinpath(*args)

    # Does the path not exist?
    if not src.isfile():
        return

    # Get the path within the Source.Python repository
    dest = SOURCE_PYTHON_DIR.joinpath(*args)

    # Does the destination not exist?
    if not dest.isfile():

        # Link the file
        link_file(src, dest)
