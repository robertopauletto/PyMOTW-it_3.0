#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__='2016-07-20'
__version__='0.1'
__doc__="""
Interfaccia grafica per lo spell check di un articolo tradotto
"""

from Tkinter import *
import ttk
from tkFileDialog import askopenfilename
from tkMessageBox import askokcancel, askquestion, askyesno
import os.path


class Gui(object):

    def __init__(self, root, geometry="800x600+100+200"):

        self.root = root
        self.root.title("Spell Checker")
        self.root.wm_iconbitmap('@spell_checking.xbm')
        if geometry:
            self.root.geometry(geometry)
        self._file = StringVar(value='Scegliere il file da correggere')
        self._draw()

    def _draw(self):
        fm = ttk.LabelFrame(self.root, text=" File da tradurre ")
        Entry(
            fm, textvariable=self._file
        ).grid(row=0, column=0, padx=5, pady=5, sticky=EW)
        Button(
            fm, text='Sfoglia'
        ).grid(row=0, column=1, padx=5, pady=5, sticky=EW)
        fm.columnconfigure(0, weight=2)

        fm.grid(row=0, column=0, padx=8, pady=8, sticky=EW)

        fmNav = ttk.LabelFrame(self.root, text=' Navigazione ')
        Button(
            fmNav, text='<<'
        ).grid(row=0, column=2, padx=5, pady=5)
        Button(
            fmNav, text='<'
        ).grid(row=0, column=3, padx=5, pady=5)
        Button(
            fmNav, text='>'
        ).grid(row=0, column=4, padx=5, pady=5)
        Button(
            fmNav, text='>>'
        ).grid(row=0, column=5, padx=5, pady=5)
        fmNav.columnconfigure(0, weight=0)
        fmNav.columnconfigure(1, weight=0)
        fmNav.columnconfigure(2, weight=1)
        fmNav.columnconfigure(3, weight=1)
        fmNav.columnconfigure(4, weight=1)
        fmNav.columnconfigure(5, weight=1)
        fmNav.grid(row=1, column=0, padx=8, pady=8, sticky=EW)


        self.root.columnconfigure(0, weight=2)


if __name__ == '__main__':
    root = Tk()
    gui = Gui(root)
    root.update_idletasks()
    root.mainloop()
