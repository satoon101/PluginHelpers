# ../plugin_releaser/paths.py

"""Stores paths used by plugin_releaser."""

# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Store all allowed readable data file types
_readable_data = [
    'ini',
    'json',
    'vdf',
    'xml',
]

# Store plugin specific directories with their respective allowed file types
allowed_filetypes = {
    'addons/source-python/plugins/': _readable_data + ['md', 'py'],
    'addons/source-python/data/plugins/': _readable_data + ['md', 'txt'],
    'cfg/source-python/': _readable_data + ['cfg', 'md', 'txt'],
    'logs/source-python/': ['md', 'txt'],
    'sound/source-python/': ['md', 'mp3', 'wav'],
    'resource/source-python/events/': ['md', 'txt'],
    'resource/source-python/translations/': ['md', 'ini'],
}

# Store non-plugin specific directories
#   with their respective allowed file types
other_filetypes = {
    'materials/': ['vmt', 'vtf'],
    'models/': ['mdl', 'phy', 'vtx', 'vvd'],
}

# Store directories with files that fit allowed_filetypes
#   with names that should not be included
exception_filetypes = {
    'resource/source-python/translations/': ['_server.ini'],
}
