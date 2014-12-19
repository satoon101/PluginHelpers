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

    print(options)
    print(args)

    print(options.name)
    print(options.config)
    print(options.data)
    print(options.events)
    print(options.logs)
    print(options.sound)
    print(options.translations)

    # 
    if options.name is None:
        print('No plugin name provided.')
        return

    # 
    PLUGINDIR = STARTDIR.joinpath(options.name)

    # 
    if PLUGINDIR.isdir():
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

    PLUGIN_BASE_PATH = PLUGINDIR.joinpath('addons', 'source-python', 'plugins')

    PLUGIN_PATH = PLUGIN_BASE_PATH.joinpath(options.name)

    PLUGIN_PATH.makedirs()

    with PLUGIN_PATH.joinpath('__init__.py').open('w') as open_file:

        write_top_lines(open_file, PLUGIN_BASE_PATH)

    with PLUGIN_PATH.joinpath(options.name + '.py').open('w') as open_file:

        write_top_lines(open_file, PLUGIN_BASE_PATH)

    with PLUGIN_PATH.joinpath('info.py').open('w') as open_file:

        write_top_lines(open_file, PLUGIN_BASE_PATH)

        write_info(open_file, options.name, author)

    # 
    #if options.config == 'True':

    # 
    #if options.data == 'file':

    # 
    #elif options.data == 'directory':

    # 
    #if options.events == 'True':

    # 
    #if options.logs == 'True':

    # 
    #if options.sound == 'True':

    # 
    #if options.translation == 'file':

    # 
    #elif options.translation == 'directory':


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
