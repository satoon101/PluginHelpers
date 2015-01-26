from tkinter import BOTH
from tkinter import CENTER
from tkinter import E
from tkinter import END
from tkinter import INSERT
from tkinter import RIGHT
from tkinter import Text
from tkinter import Tk
from tkinter import YES
from tkinter.ttk import Button
from tkinter.ttk import Frame
from tkinter.ttk import Label

class Unsupported(Tk):

    def exit_unsupported(self, version_info):
        version = '.'.join(map(str, version_info[:3]))
        text = Text(self.master)
        text.config(font=('times', 10, 'bold'))
        text.tag_configure('red', foreground='red')
        text.tag_configure('black', foreground='black')
        text.insert(
            INSERT, 'Unsupported Python version "', 'black')
        text.insert(END, '{0}'.format(version), 'red')
        text.insert(END, '"', 'black')
        text.tag_add('center', 1.0, 'end')
        text.tag_configure('center', justify='center')
        text.pack()
        self.title('Error')
        exit_button = Button(self, text='Exit', command=self.quit)
        exit_button.place(x=80, y=50)
        self.mainloop()

unsupported = Unsupported()
unsupported.geometry('240x100')
