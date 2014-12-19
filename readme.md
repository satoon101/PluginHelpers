# Source.Python PluginHelpers

## Introduction
PluginHelpers is a set of tools to be used with [Source.Python](https://github.com/Source-Python-Dev-Team/Source.Python) plugins.

<br>
## Configuration
The first thing you need to do is execute the config.bat file to create the config.ini file.
The current configuration values are:
```ini
# Set to the directory that your server's are located in.
SERVERSTARTDIR="C:\Servers"

# Set to the directory where your releases should be placed.
RELEASEDIR="C:\Releases"

# Set to your nickname.
# This value is used to assign the author variable when creating a plugin.
AUTHOR=""
```

* SERVERSTARTDIR is used by the PluginLinker to know what directory your server's are located in.
* RELEASEDIR is used by the PluginReleaser to know where to copy your plugin releases to.
* AUTHOR is used by the PluginCreater to know what value to put as info.author for the plugin.

<br>
## Setup
The PluginCreater, PluginChecker, and PluginReleaser will function just fine without having a test server linked.
However, linking a test server will help to not have to copy/paste files over and over when you make changes.
In order for all of these helpers to be truly helpful, there are certain criteria your test setup has to adhere to.

* The test servers must be located on the same drive as the plugins directory.
    * The reason for this is that creating symbolic links for files (not directories) requires the file to be on the same drive as the linked file.
    * If any of your plugins contains one of the following, trying to create a symbolic link will not work:
        * ..\addons\source-python\data\&lt;plugin_name&gt;.ini
        * ..\resource\source-python\translations\&lt;plugin_name&gt;.ini
* Each server's main folder must be named the same as the [GAME_NAME](http://wiki.sourcepython.com/pages/core#GAME_NAME) value.
    * For example, cstrike should be in:
        * &lt;SERVERSTARTDIR&gt;\cstrike\
    * where Source.Python is installed at:
        * &lt;SERVERSTARTDIR&gt;\cstrike\cstrike\addons\source-python\
* [Python3.4](https://www.python.org/downloads/) or newer needs to be installed and it's path added to the Path environment variable.
* The [configobj](https://github.com/DiffSK/configobj) package needs to be installed in your Python installation.
* The [path.py](https://github.com/jaraco/path.py) package needs to be installed in your Python installation.

<br>
## Available helpers

### PluginCreater
The plugin_creater.bat file is used to create a plugin based on the name provided.

### PluginChecker
The plugin_checker.bat file, along with the .pylintrc file, is used to perform standards checks (like PEP8 and PEP257) on the chosen plugin.

### PluginLinker
The plugin_linker.bat file is used to create symbolic links for all plugins on the chosen server.

### PluginReleaser
The plugin_releaser.bat file is used to create a zip file for a new release of the chosen plugin.

<br>
## Usage

### PluginCreater
After you have completed the setup portion, you will want to create a plugin.

Execute the plugin_creater.bat and answer the questions that follow.

For the 'name' of the plugin, only alpha-numeric values, as well as underscores, are allowed.
If you choose to create a cfg, events, or logs directory, an empty readme.md file will be created as a place-holder.

### PluginLinker
Once you have created your plugin, and gotten it to a point where you think it should work in-game, the next step is to execute the plugin_linker.bat file to link it to one or more of your servers.

### PluginChecker
Before you release your plugin, you should run the plugin_checker.bat to find and fix any standards issues.  You could have done this prior to linking, as well, but just be sure to use it prior to releasing.

The plugin_checker allows you to select which plugin to check.  Once you have chosen the plugin, it will run the following checkers:
*[pep8](https://pypi.python.org/pypi/pep8)
*[pep257](https://pypi.python.org/pypi/pep257)
*[pyflakes](https://pypi.python.org/pypi/pyflakes)
*[pylint](https://pypi.python.org/pypi/pylint)

### PluginReleaser
Now that you have tested your plugin on a server and run the standards checks, it is time to create release.

Just run the plugin_releaser.bat file and select the plugin you wish to release.

All releases will be created in the directory you assigned RELEASEDIR to in your config.ini file.

The directory structure used by plugin_releaser is &lt;RELEASEDIR&gt;\&lt;plugin_name&gt;\&lt;plugin_name&gt;_v&lt;plugin_version&gt;.zip
