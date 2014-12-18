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
    '-c', '--config', default=None, help='Add config directory')

# Create the 'data' option
option_parser.add_option(
    '-d', '--data', default=None, help='Add data file or directory')

# Create the 'translations' option
option_parser.add_option(
    '-t', '--translations', default=None,
    help='Add translation file or directory')
