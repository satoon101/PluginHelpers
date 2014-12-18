# ../plugin_releaser/__main__.py

""""""

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
from plugin_releaser import main


# =============================================================================
# >> CALL MAIN
# =============================================================================
if __name__ == '__main__':
    main()
