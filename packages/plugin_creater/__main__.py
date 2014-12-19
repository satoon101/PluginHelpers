# ../plugin_creater/__main__.py

"""Used by Python to call plugin_creater from the command line."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import sys

# Site-Package Imports
#   Path
from path import Path

# Add the package path to sys.path
sys.path.append(Path(__file__).parent.parent)

# Package Imports
from plugin_creater import create_plugin
from plugin_creater.options import option_parser


# =============================================================================
# >> CALL MAIN FUNCTION
# =============================================================================
if __name__ == '__main__':

    # Get the options used
    options = option_parser.parse_args()

    # Call create_plugin with the options
    create_plugin(**vars(options))
