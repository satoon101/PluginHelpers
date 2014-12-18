# ../plugin_releaser/__main__.py

""""""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
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
from plugin_releaser.paths import allowed_filetypes
from plugin_releaser.paths import exception_filetypes
from plugin_releaser.paths import other_filetypes
from plugin_releaser.options import option_parser


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def main():
    """"""
    # 
    options, args = option_parser.parse_args()

    # 
    if options.name is None:
        print('No plugin name provided.')
        return

    # 
    startdir = Path(__file__).parent.parent.parent

    # 
    config_file = startdir.joinpath('config.ini')

    # 
    if not config_file.isfile():
        print('config.ini file not found.')
        return

    # 
    plugin_path = startdir.joinpath(options.name)

    # 
    if not plugin_path.isdir():
        print('Plugin "{0}" not found.'.format(options.name))
        return

    try:

        release_path = ConfigObj(config_file)['RELEASEDIR']

    except KeyError:
        print('No release path found in config.ini.')
        return

    except ConfigObjError:
        print('config.ini has errors, please remove and re-run config.bat')
        return

    version = get_version(plugin_path.joinpath(
        'addons', 'source-python', 'plugins', options.name))

    if version is None:
        print('No version found.')
        return

    save_path = Path(release_path).joinpath(options.name)

    if not save_path.isdir():
        save_path.makedirs()

    zip_path = save_path.joinpath(
        '{0} - v{1}.zip'.format(options.name, version))

    if zip_path.isfile():
        print('Release already exists for current version.')
        return

    print(zip_path)


def get_version(plugin_path):
    """"""
    # 
    for file in plugin_path.files('*.py'):

        # 
        with file.open() as open_file:

            # 
            contents = open_file.read()

            # 
            if 'info.version = ' not in contents:
                continue

            value = contents.split('info.version = ', 1)[1]

            value = value.splitlines()[0]

            return value[1:~0]

    return None
