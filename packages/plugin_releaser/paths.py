# ../plugin_releaser/__main__.py

""""""

# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# 
_readable_data = [
    'ini',
    'json',
    'vdf',
    'xml',
]

allowed_filetypes = {

    # 
    'addons/source-python/plugins/': _readable_data + ['py'],

    # 
    'addons/source-python/data/plugins/': _readable_data + ['txt'],

    # 
    'cfg/source-python/': _readable_data + ['cfg', 'txt'],

    # 
    'logs/source-python/': ['txt'],

    # 
    'sound/source-python/': ['mp3', 'wav'],

    # 
    'resource/source-python/events/': ['txt'],

    # 
    'resource/source-python/translations/': ['ini'],
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
