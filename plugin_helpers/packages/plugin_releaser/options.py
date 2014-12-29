# ../plugin_releaser/options.py

"""Creates the options used by plugin_releaser."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   ArgParse
from argparse import ArgumentParser


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Create the options
option_parser = ArgumentParser()

# Create the 'name' option
option_parser.add_argument(
    '--name', dest='plugin_name', help='The name of the plugin.')
