# ../plugin_creater/options.py

""""""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   OptParse
from optparse import OptionParser


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Create the options
option_parser = OptionParser()

# Create the 'name' option
option_parser.add_option(
    '-n', '--name', default=None, help='The name of the plugin')

# Create the 'config' option
option_parser.add_option(
    '-c', '--config', default=None,
    choices=['True', 'False'], help='Add config directory')

# Create the 'data' option
option_parser.add_option(
    '-d', '--data', default=None,
    choices=['file', 'directory'], help='Add data file or directory')

# Create the 'events' option
option_parser.add_option(
    '-e', '--events', default=None,
    choices=['True', 'False'], help='Add events directory')

# Create the 'logs' option
option_parser.add_option(
    '-l', '--logs', default=None,
    choices=['True', 'False'], help='Add logs directory')

# Create the 'sound' option
option_parser.add_option(
    '-s', '--sound', default=None,
    choices=['True', 'False'], help='Add sound directory')

# Create the 'translations' option
option_parser.add_option(
    '-t', '--translations', default=None,
    choices=['file', 'directory'], help='Add translation file or directory')
