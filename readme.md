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
```

* SERVERSTARTDIR is used by the PluginLinker to know what directory your server's are located in.
* RELEASEDIR is used by the PluginReleaser to know where to copy your plugin releases to.

<br>
## Setup
The PluginCreater, PluginChecker, and PluginReleaser will function just fine without having a test server linked.
However, linking a test server will help to not have to copy/paste files over and over when you make changes.
In order for all of these helpers to be truly helpful, there are certain criteria your test server has to adhere to.

* The test servers must be located on the same drive as the plugins directory.
* Each server's main folder must be named the same as the [GAME_NAME](http://wiki.sourcepython.com/pages/core#GAME_NAME) value.
    * For example, cstrike should be in:
        * <<1>SERVERSTARTDIR>\cstrike\
    * where Source.Python is installed at:
        * <<1>SERVERSTARTDIR>\cstrike\cstrike\addons\source-python\

<br>
## Available helpers

### PluginCreater
The plugin_creator.bat file, along with the plugin_creator.py file, is used to create a plugin based on the name provided.

### PluginChecker
The plugin_checker.bat file, along with the .pylintrc file, is used to perform standards checks (like PEP8 and PEP257) on the chosen plugin.

### PluginLinker
The plugin_linker.bat file is used to create symbolic links for all scripts on the chosen server.

### PluginReleaser
The plugin_releaser.bat file, along with the plugin_releaser.py file, is used to create a zip file for a new release of the chosen plugin.
