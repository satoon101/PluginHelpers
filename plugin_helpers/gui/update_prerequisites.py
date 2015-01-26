import os
from sys import executable
from tkinter import Button
from tkinter import Frame
from common.constants import START_DIR
from common.interface import MainPage
from common.interface import interface


class Prerequisites(Frame):

    """"""

    def __init__(self, parent, controller):
        """"""
        super(Prerequisites, self).__init__(parent)
        button = Button(
            self, text='Back', command=lambda: interface.show_frame(MainPage))
        button.pack()

interface.frames[MainPage].register_frame(Prerequisites)
#os.system('{0} -m pip install --upgrade -r {1}'.format(
#    executable, START_DIR.joinpath('plugin_helpers', 'tools', 'requirements.txt')))
