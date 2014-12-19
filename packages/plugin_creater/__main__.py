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
from plugin_creater import main
from plugin_creater.options import option_parser


# =============================================================================
# >> CALL MAIN
# =============================================================================
if __name__ == '__main__':

    # Get the options used
    kwargs, args = option_parser.parse_args()

    # Call main with the options
    main(*args, **kwargs)
