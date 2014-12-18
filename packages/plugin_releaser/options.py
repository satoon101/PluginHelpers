# ../plugin_releaser/options.py

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
