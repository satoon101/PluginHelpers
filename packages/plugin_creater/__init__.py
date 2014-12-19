# ../plugin_creater/__init__.py

""""""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   OptParse
from optparse import OptionParser

# Site-Package Imports
#   Configobj
from configobj import ConfigObj
from configobj import ConfigObjError
#   Path
from path import Path

# Package Imports
from plugin_creater.paths import CONFIG_FILE
from plugin_creater.paths import STARTDIR
from plugin_creater.options import option_parser


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
    if not options.name.replace('_', '').isalnum():
        print('Invalid plugin name.')
        print(
            'Plugin name must only contain ' +
            'alpha-numeric values and underscores.')
        return

    # 
    plugin_base_path = STARTDIR.joinpath(options.name)

    # 
    if plugin_base_path.isdir():
        print('Plugin already exists.')
        return

    # 
    if not CONFIG_FILE.isfile():
        print('config.ini file not found, please run config.bat.')
        return

    try:

        author = ConfigObj(CONFIG_FILE)['AUTHOR']

    except KeyError:
        print('No author found in config.ini.')
        print('Please delete config.ini and re-run config.bat.')
        return

    except ConfigObjError:
        print('config.ini has errors.')
        print('Please delete config.ini and re-run config.bat.')
        return

    plugin_home_path = plugin_base_path.joinpath(
        'addons', 'source-python', 'plugins')

    plugin_path = plugin_home_path.joinpath(options.name)

    plugin_path.makedirs()

    with plugin_path.joinpath('__init__.py').open('w') as open_file:

        write_top_lines(open_file, plugin_home_path)

    with plugin_path.joinpath(options.name + '.py').open('w') as open_file:

        write_top_lines(open_file, plugin_home_path)

    with plugin_path.joinpath('info.py').open('w') as open_file:

        write_top_lines(open_file, plugin_home_path)

        write_info(open_file, options.name, author)

    # 
    if options.config == 'True':

        config_path = plugin_base_path.joinpath(
            'cfg', 'source-python', options.name)

        config_path.makedirs()

        config_path.joinpath('readme.md').touch()

    # 
    if options.data == 'file':

        data_path = plugin_base_path.joinpath(
            'addons', 'source-python', 'data', 'plugins')

        data_path.makedirs()

        data_path.joinpath(options.name + '.ini').touch()

    # 
    elif options.data == 'directory':

        plugin_base_path.joinpath(
            'addons', 'source-python', 'data',
            'plugins', options.name).makedirs()

    # 
    if options.events == 'True':

        events_path = plugin_base_path.joinpath(
            'resource', 'source-python', 'events', options.name)

        events_path.makedirs()

        events_path.joinpath('readme.md').touch()

    # 
    if options.logs == 'True':

        logs_path = plugin_base_path.joinpath(
            'logs', 'source-python', options.name)

        logs_path.makedirs()

        logs_path.joinpath('readme.md').touch()

    # 
    if options.sound == 'True':

        plugin_base_path.joinpath(
            'sound', 'source-python', options.name).makedirs()

    # 
    if options.translations == 'file':

        translations_path = plugin_base_path.joinpath(
            'resource', 'source-python', 'translations')

        translations_path.makedirs()

        translations_path.joinpath(options.name + '.ini').touch()

    # 
    elif options.translations == 'directory':

        plugin_base_path.joinpath(
            'resource', 'source-python',
            'translations', options.name).makedirs()


def write_top_lines(open_file, path):
    """"""
    # 
    open_file.write('# ..{0}\n\n"""."""\n\n'.format(
        open_file.name.split(path, 1)[1].replace('\\', '/')))


def write_info(open_file, plugin_name, author):
    """"""
    # 
    separator = '# {0}\n'.format('=' * 77)
    open_file.write(separator)
    open_file.write('# >> IMPORTS\n')
    open_file.write(separator)

    # 
    open_file.write('# Source.Python Imports\n')
    open_file.write('#   Cvars\n')
    open_file.write('from cvars.public import PublicConVar\n')
    open_file.write('#   Plugins\n')
    open_file.write('from plugins.info import PluginInfo\n\n\n')

    # 
    open_file.write(separator)
    open_file.write('# >> PLUGIN INFO\n')
    open_file.write(separator)

    # 
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


if __name__ == '__main__':
    main()
