# ../plugin_creater/options.py

"""Creates the options used by plugin_creater."""

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

# Create the 'config' option
option_parser.add_argument(
    '--config', action='store_const', const=True,
    help='Whether a config directory should be added.')

# Create the 'data' option
option_parser.add_argument(
    '--data', choices=['file', 'directory'],
    help='Whether a data file or directory should be added.')

# Create the 'events' option
option_parser.add_argument(
    '--events', action='store_const', const=True,
    help='Whether a events directory should be added.')

# Create the 'logs' option
option_parser.add_argument(
    '--logs', action='store_const', const=True,
    help='Whether a logs directory should be added.')

# Create the 'sound' option
option_parser.add_argument(
    '--sound', action='store_const', const=True,
    help='Whether a sound directory should be added.')

# Create the 'translations' option
option_parser.add_argument(
    '--translations', choices=['file', 'directory'],
    help='Whether a translation file or directory should be added.')
