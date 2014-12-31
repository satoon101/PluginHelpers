# Source.Python PluginHelpers

## Introduction
PluginHelpers is a set of tools to be used with [Source.Python](https://github.com/Source-Python-Dev-Team/Source.Python) plugins.

These tools allow you to do the following:
* Create a new Source.Python plugin.
* Check your plugins for any standards issues.
* Link Source.Python to your test servers and link your plugins to Source.Python.
* Create a release .zip file for your plugins.

<br>
## Pre-Setup
Before you get started, there are a few things you will need installed and a few guidelines you need to follow.
* Git
    * Obviously, since this is a git repository, this is going to be necessary.
    * On Windows, install either Git Bash or TortoiseGit (or both).
    * On Linux, use yum or apt-get to install 'git'.
* Python3.4 or newer
    * Python3.4 is the version being tested with when making changes.
    * I do not plan on testing earlier versions to support them.
    * If you will be using this on a Linux system, most distros come with some version of Python2.  When you install Python3.4, make sure you do not make it the systems default, as that can and will cause you issues.
    * I have found the following to be a good guide to installing Python3.4 on Linux:
        * http://www.unixmen.com/howto-install-python-3-x-in-ubuntu-debian-fedora-centos/
        * Though, the wget and tar lines should look more like:

            ```
wget https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tgz
tar -xjf Python-3.4.2.tgz cd Python-3.4.2
            ```

* Source-engine servers
    * The guideline on servers is that they need to follow a simple rule.
        * Each server must have a directory named the exact same as the [GAME_NAME](http://wiki.sourcepython.com/pages/core#GAME_NAME) value for the game.
        * For instance, Counter-Strike: Source servers are installed in a directory called 'cstrike'.  So, the hosting directory needs to use that same name.
        * If your servers are located in **C:\Servers\**, CS:S needs to be installed in **C:\Servers\cstrike\\**.
        * As a reference, the SteamCMD runscript should have values similar to the following:

            ```
            login anonymous

            // CS:S
            force_install_dir ../cstrike/
            app_update 232330 validate

            // DOD:S
            force_install_dir ../dod/
            app_update 232290 validate

            // HL2:DM
            force_install_dir ../hl2mp/
            app_update 232370 validate

            // TF2
            force_install_dir ../tf/
            app_update 232250 validate

            // CS:GO
            force_install_dir ../csgo/
            app_update 740 validate

            exit
            ```

* Source.Python clone
    * Simply use git to clone [Source.Python](https://github.com/Source-Python-Dev-Team/Source.Python).
    * The Source.Python clone **must** be on the same drive as this repository.
        * If they are on 2 different drives, hard links can not be created for your plugins.
        * symlinks (soft links) will work fine for directory linking, but hard links for files will not.
        * Since the linking of the Source.Python repository to the servers is done with only symlinks, it is not necessary that the servers be on the same drive.
        * None of this matters on Linux systems.

<br>
## Setup
The first thing you need to do after cloning the repository is to execute the setup file (.bat for Windows or .sh for Linux).
After you have done this, several new files will be created in the main directory.
Those files include the config.ini, which holds configuration values you need to set, and a .pylintrc file which can be used for different pytlint settings when running the **plugin_checker** script.
A few platform-specific (.bat for Windows or .sh for Linux) files are also created:
* plugin_checker
* plugin_creater
* plugin_linker
* plugin_releaser
* prerequisites
* server_linker

<br>
## Configuration
The next step is to set up your configuration values.  Open the config.ini and set the values appropriately.
The following are the settings

* AUTHOR
    * used by **plugin_creater** to know what value to put as info.author for the plugin.
* REPOTYPE
    * used by **plugin_creater** to know whether to create the .gitignore / .gitattributes or .hgignore files.
* SERVERSTARTDIR
    * used by **server_linker** to know where your server's are located.
    * Defaults:
        * Windows: **C:\Servers**
        * Linux: **/media/Servers**
* SOURCEPYTHONDIR
    * used by **plugin_linker** and **server_linker** to know where the Source.Python repository is located.
    * Defaults:
        * Windows: **C:\Projects\Source.Python**
        * Linux: **/media/Source.Python**
* RELEASEDIR
    * used by **plugin_releaser** to know where to copy your plugin releases to.
    * Defaults:
        * Windows: **C:\Releases**
        * Linux: **/media/Releases**
* PYTHONEXE
    * used by all of the executables (including prerequisites) to know where the Python executable is located.
    * This needs to be set to the executable file itself and not just its directory.
    * Defaults:
        * Windows: **C:\Python34\python**
        * Linux: **/opt/python3/bin/python3.4**

<br>
## Prerequisite packages
After you have your configuration set, execute the prerequisite script to install the required Python packages.

The required packages for this toolset include:
* [configobj](https://github.com/DiffSK/configobj)
    * used by the Python scripts to get your configuration values.
* [path.py](https://github.com/jaraco/path.py)
    * used by the Python scripts to more easily navigate directories and files on your system.
* [pep8](https://pypi.python.org/pypi/pep8)
    * used by the **plugin_checker** script to check for any PEP8 violations in your plugins.
* [pep257](https://pypi.python.org/pypi/pep257)
    * used by the **plugin_checker** script to check for any PEP257 violations in your plugins.
* [pyflakes](https://pypi.python.org/pypi/pyflakes)
    * used by the **plugin_checker** script to check your plugins for a few different issues.
* [pylint](https://pypi.python.org/pypi/pylint)
    * used by the **plugin_checker** script to check your plugins for a lot of different issues.

<br>
## Linking Source.Python
Once you have finished installing the prerequisites, the next item on the list is to link Source.Python's repository to your servers.

As long as you have correctly set your config.ini SERVERSTARTDIR, SOURCEPYTHONDIR, and PYTHONEXE values, simply execute the **server_linker** script and select the server you wish to link (or ALL for all servers).

<br>
## Installing plugins
If you already have some plugins started, you can copy them into the PluginHelpers repository directory.  Though, they **must** adhere to some guidelines:
* The directory name needs to be the name of the plugin (the **sp load** name).
* The internal directories need to match that of Source.Python's internal directory structure.
    * There must be a directory within the main directory that is named **addons** and contains the following directory structure **../addons/source-python/plugins/&lt;plugin_name&gt;/**.
    * Within the above directory, there must be at least a **&lt;plugin_name&gt;.py** file and an **\__init__.py** file.
* It is recommended that you have a public or private repository to host your plugin, but that is not necessary.

<br>
## Creating plugins
PluginHelpers comes with a script that helps to start the creation of new plugins.  Execute the **plugin_creater** script and answer the questions that follow.

Once you have answered all the necessary questions, the appropriate directories/files will be created.

3 files will always be created:
* \__init__.py
    * mandatory for the **plugin_checker** to work.
    * useful for verifying implementation on a server prior to loading your plugin.
* info.py
    * holds the [PluginInfo](http://wiki.sourcepython.com/pages/plugins.info#PluginInfo) instance for your plugin.
    * If you supplied an AUTHOR value in the config.ini, that value will be used as info.author.
* &lt;plugin_name&gt;.py
    * mandatory file when using the **sp load** command on a server.

<br>
## Linking plugins
Now that you have one or more plugins inside the PluginHelpers repository directory, you will want to link them to the Source.Python repository.

Linking your plugins to the Source.Python repository instead of each server individually allows you to only have to link them once and have them available on all of your test servers.

Execute the **plugin_linker** script and choose which plugin (or ALL plugins) to link.  If you have already linked a plugin, but have added new directories, running the linker again will link those directories.

<br>
## Checking plugins
At some point, or many different points, you might want to check your plugins to see if they match a set of standards (like PEP8 or PEP257).

Execute the **plugin_checker** script and choose which plugin (or ALL plugins) to check and all of the issues/errors/warnings will be shown.

<br>
## Creating a release
Once you get to a point where you think a plugin is ready to be released, execute the **plugin_releaser** script.

Select which plugin to release, or ALL plugins, if you wish to create a release for all of them.

The release .zip file location will be shown, and uses the RELEASEDIR value from the config.ini.

The **plugin_releaser** script does use the info.version value that needs to be set somewhere in your Python code for that script.

Each release is saved as **&lt;RELEASEDIR&gt;/&lt;plugin_name&gt;/&lt;plugin_name&gt;_v&lt;version&gt;.zip**, so that if you have a plugin named my_plugin and its version is 1.0, the file would be **&lt;RELEASEDIR&gt;/my_plugin/my_plugin_v1.0.zip**.
