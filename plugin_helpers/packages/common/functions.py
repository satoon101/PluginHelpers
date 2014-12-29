# ../common/functions.py

"""Provides commonly used functions."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Contextlib
from contextlib import suppress
#   OS
from os import system

# Package Imports
from common.constants import PLATFORM
from common.constants import plugin_list
from common.constants import server_list


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def clear_screen():
    """Clear the screen."""
    system('cls' if PLATFORM == 'windows' else 'clear')


def get_plugin(suffix, allow_all=True):
    """Return a plugin by name to do something with."""
    # Clear the screen
    clear_screen()

    # Are there any plugins?
    if not plugin_list:
        print('There are no plugins to {0}.'.format(suffix))
        return None

    # Get the question to ask
    message = 'What plugin would you like to {0}?\n\n'.format(suffix)

    # Loop through each plugin
    for number, plugin in enumerate(plugin_list, 1):

        # Add the current plugin
        message += '\t({0}) {1}\n'.format(number, plugin)

    # Add ALL to the list if it needs to be
    if allow_all:
        message += '\t({0}) ALL\n'.format(len(plugin_list) + 1)

    # Ask which plugin to do something with
    value = input(message + '\n').strip()

    # Was a plugin name given?
    if value in plugin_list + ['ALL']:

        # Return the value
        return value

    # Was an integer given?
    with suppress(ValueError):

        # Typecast the value
        value = int(value)

        # Was the value a valid plugin choice?
        if value <= len(plugin_list):

            # Return the plugin by index
            return plugin_list[value - 1]

        # Was ALL's choice given?
        if value == len(plugin_list) + 1 and allow_all:

            # Return ALL
            return 'ALL'

    # If no valid choice was given, try again
    return get_plugin(suffix, allow_all)


def get_server():
    """Return a server to do something with."""
    # Clear the screen
    clear_screen()

    # Are there any servers?
    if not server_list:
        print('There are no servers to link.')
        return None

    # Get the question to ask
    message = 'Which server would you like to link?\n\n'

    # Loop through each server
    for number, server in enumerate(server_list, 1):

        # Add the current server
        message += '\t({0}) {1}\n'.format(number, server)

    # Add ALL to the list
    message += '\t({0}) ALL\n'.format(len(server_list) + 1)

    # Ask which server to do something with
    value = input(message + '\n').strip()

    # Was a server name given?
    if value in server_list + ['ALL']:

        # Return the value
        return value

    # Was an integer given?
    if isinstance(value, int):

        # Was the value a valid server choice?
        if value <= len(server_list):

            # Return the server by index
            return server_list[value]

        # Was ALL's choice given?
        if value == len(server_list) + 1:

            # Return ALL
            return 'ALL'

    # If no valid choice was given, try again
    return get_server()
