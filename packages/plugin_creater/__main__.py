from optparse import OptionParser
from path import Path


STARTDIR = Path(__file__).parent


option_parser = OptionParser()

option_parser.add_option(
    '-n', '--name', default=None, help='The name of the plugin')

option_parser.add_option(
    '-c', '--config', default=None, help='Add config directory')

option_parser.add_option(
    '-d', '--data', default=None, help='Add data file or directory')

option_parser.add_option(
    '-t', '--translations', default=None,
    help='Add translation file or directory')

from sys import argv

print(argv)

def main():
    """"""
    # 
    options, args = option_parser.parse_args()

    print(options)
    print(args)

    # 
    plugin_name = args[0]

    print(plugin_name)
    print(options.config)
    print(options.data)
    print(options.translations)

    # 
    if plugin_name is None:
        print('No plugin name provided.')
        return

    # 
    PLUGINDIR = STARTDIR.joinpath(plugin_name)

    # 
    if PLUGINDIR.isdir():
        print('Plugin already exists.')
        return

    # 
    #if options['config'] == 'True':

    # 
    #if options.data == 'file':

    # 
    #elif options.data == 'directory':

    # 
    #if options.translation == 'file':

    # 
    #elif options.translation == 'directory':


if __name__ == '__main__':
    main()
