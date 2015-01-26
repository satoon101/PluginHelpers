# ../common/interface.py

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Collections
from collections import OrderedDict
#   Importlib
from importlib import import_module
#   Tkinter
from tkinter import BOTH
from tkinter import Tk
from tkinter import W
from tkinter.ttk import Button
from tkinter.ttk import Frame
from tkinter.ttk import Label

# Site-Package Imports
#   Path
from path import Path


# =============================================================================
# >> CLASSES
# =============================================================================
class Interface(Tk):

    """"""

    def __init__(self):
        """"""
        super(Interface, self).__init__()
        self.container = Frame(self)
        self._frames = dict()

    @property
    def frames(self):
        """"""
        return self._frames

    def show_frame(self, container):
        """"""
        frame = self.frames[container]
        print('Raising {0}'.format(frame))
        frame.tkraise()

    def register_frame(self, frame_class):
        """"""
        if frame_class in self.frames:
            raise
        frame = frame_class(self.container, self)
        self.frames[frame_class] = frame
        frame.grid(row=0, column=0, sticky='nsew')
        return frame

interface = Interface()
interface.geometry('800x400')

class MainPage(Frame):

    def __init__(self, parent, controller):
        super(MainPage, self).__init__(parent)
        self._frames = OrderedDict()

    @property
    def frames(self):
        return self._frames

    def register_frame(self, frame_class):
        print('registering {0}'.format(frame_class))
        if frame_class in self.frames:
            raise
        frame = interface.register_frame(frame_class)
        self.frames[frame_class] = frame

    def tkraise(self):
        for name, command in self.frames.items():
            print(name.__name__, command)
            button = Button(self, text=name.__name__, command=command)
            button.pack()
        super(MainPage, self).tkraise()

interface.register_frame(MainPage)

# Import all modules to create the full interface
for _file in Path(__file__).parent.parent.files():
    if _file.namebase.startswith('_'):
        continue
    import_module(_file.namebase)
