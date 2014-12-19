# ../plugin_releaser/paths.py

""""""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Site-Package Imports
#   Path
from path import Path


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# 
STARTDIR = Path(__file__).parent.parent.parent

# 
CONFIG_FILE = STARTDIR.joinpath('config.ini')

# 
_readable_data = [
    'ini',
    'json',
    'vdf',
    'xml',
]

allowed_filetypes = {

    # 
    'addons/source-python/plugins/': _readable_data + ['md', 'py'],

    # 
    'addons/source-python/data/plugins/': _readable_data + ['md', 'txt'],

    # 
    'cfg/source-python/': _readable_data + ['cfg', 'md', 'txt'],

    # 
    'logs/source-python/': ['md', 'txt'],

    # 
    'sound/source-python/': ['md', 'mp3', 'wav'],

    # 
    'resource/source-python/events/': ['md', 'txt'],

    # 
    'resource/source-python/translations/': ['md', 'ini'],
}

other_filetypes = {

    # 
    'materials/': ['vmt', 'vtf'],

    # 
    'models/': ['mdl', 'phy', 'vtx', 'vvd'],
}

exception_filetypes = {

    # 
    'resource/source-python/translations/': ['_server.ini'],
}
