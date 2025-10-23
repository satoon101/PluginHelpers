# ../plugin_checker.py

"""Checks plugins for standards issues."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
import sys
import tkinter as tk

# Package
from common.constants import PLUGIN_LIST, START_DIR, config
from common.interface import BaseInterface


# =============================================================================
# >> CLASSES
# =============================================================================
class Interface(BaseInterface):

    name = "Plugin Checker"
    stdout = sys.stdout
    stderr = sys.stderr

    def run(self):
        self.window.title(self.name)
        self.clear_grid()
        self.create_grid(data=PLUGIN_LIST)
        self.add_back_button(self.on_back_to_main)

    def on_click(self, option):
        self.clear_grid()
        console = self.get_console()
        plugin_path = START_DIR.joinpath(
            option,
            config["PLUGIN_BASE_PATH"],
            option,
        )
        self.execute_console_commands(
            console=console,
            commands=[f"ruff check {plugin_path}"],
        )
        refresh_button = tk.Button(
            self.window,
            text="Refresh",
            command=lambda o=option: self.on_click(o),
        )
        refresh_button.place(x=445, y=730)
        self.add_back_button(self.run)
