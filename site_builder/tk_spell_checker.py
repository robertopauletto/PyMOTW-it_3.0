#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__='2016-07-20'
__version__='0.1'
__doc__="""
Interfaccia grafica per lo spell check di un articolo tradotto
"""

from Tkinter import *
from tkFileDialog import askopenfilename
from tkMessageBox import askokcancel, askquestion, askyesno
import os.path


class Gui(object):

    def __init__(self, root, geometry="800x600+100+200"):

        self.root = root
        self.root.title("Spell Checker")
        self.root.wm_iconbitmap('@spell_checking.xbm')
        self.root.geometry(geometry)
        self._file = StringVar(value='Scegliere il file da correggere')
        self._draw()

    def _draw(self):
        fm = LabelFrame(
            self.root, text=" File da tradurre "
        )
        Entry(
            fm, textvariable=self._file
        ).grid(row=0, column=0, padx=5, pady=5, sticky=EW)
        Button(
            fm, text='Sfoglia'
        ).grid(row=0, column=1, padx=5, pady=5, sticky=EW)

        fm.grid(row=0, column=0, padx=8, pady=8, sticky=EW)

if __name__ == '__main__':
    root = Tk()
    gui = Gui(root)
    root.update_idletasks()
    root.mainloop()
