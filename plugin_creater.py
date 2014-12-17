from optparse import OptionParser
from path import Path


STARTDIR = Path(__file__).parent


option_parser = OptionParser()

option_parser.add_option(
    '-n', '--name', default=None, help='The name of the plugin')

option_parser.add_option(
    '-c', '--config', default=None, help='Add config file or directory')

option_parser.add_option(
    '-t', '--translation', default=None,
    help='Add translation file or directory')


def main():
    """"""
    # 
    options, args = option_parser.parse_args()

    # 
    plugin_name = options['name']

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
    if options['config'] == 'file':

    # 
    elif options['config'] == 'directory':

    # 
    if options['translation'] == 'file':

    # 
    elif options['translation'] == 'directory':


if __name__ == '__main__':
    main()
