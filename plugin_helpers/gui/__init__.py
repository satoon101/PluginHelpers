# ../__init__.py

"""This file is necessary for the package_checker to work properly."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Sys
import sys


# =============================================================================
# >> MAIN FUNCTION
# =============================================================================
def show_gui():
    """"""
    # Is the version of Python invalid?
    if sys.version_info < (3, 4):

        # Show the error and exit
        from common.unsupported import unsupported
        unsupported.exit_unsupported(sys.version_info)
        return

    # Show the main menu
    from common.interface import MainPage
    from common.interface import interface
    interface.show_frame(MainPage)
    interface.mainloop()


'''
    Verify the Python version:
        contextlib.suppress wasn't introduced till 3.4

        If not 3.4 or newer, show an error and an exit button

    Import the modules

        Modules register as buttons

        Modules import from common

            common.settings should contain all the settings
            settings should be stored in a db file
            setting should also register a drop-down menu

    If any settings are not stored:

        Ask for setting (showing a possible value/default)
        Steam directories should have multiple input boxes (6?)

    Once all settings have been set, show buttons for each registered module
'''
