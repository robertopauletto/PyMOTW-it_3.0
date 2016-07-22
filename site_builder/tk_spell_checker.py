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

        self._new_word = StringVar()
        self._txt = None
        self._lbhints = None
        self.root = root
        self.root.title("Spell Checker")
        self.root.wm_iconbitmap('@spell_checking.xbm')
        if geometry:
            self.root.geometry(geometry)
        self._file = StringVar(value='Scegliere il file da correggere')
        self._draw()
        self._fill_hints(None)

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

        # ------------------------------------------------------

        fm_hud = ttk.LabelFrame(self.root, text=" Comandi e Navigazione ")

        fm_nv = ttk.LabelFrame(fm_hud, text=' Navigazione ')
        Button(
            fm_nv, text='<<'
        ).grid(row=0, column=0, padx=5, pady=5)
        Button(
            fm_nv, text='<'
        ).grid(row=0, column=1, padx=5, pady=5)
        Button(
            fm_nv, text='>'
        ).grid(row=0, column=2, padx=5, pady=5)
        Button(
            fm_nv, text='>>'
        ).grid(row=0, column=3, padx=5, pady=5)
        fm_nv.grid(row=0, column=0, ipady=17)

        # ------------------------------------------------------

        fm_cmd = ttk.LabelFrame(fm_hud, text=' Comandi ')
        Entry(
            fm_cmd, width=20, textvariable=self._new_word
        ).grid(row=0, column=0, padx=5, pady=5)
        Button(
            fm_cmd, text='Correggi', command=self._correggi, width=10
        ).grid(row=0, column=1, padx=5, pady=5)
        Button(
            fm_cmd, text='Ignora', command=self._correggi, width=10
        ).grid(row=0, column=2, padx=5, pady=5)
        Button(
            fm_cmd, text='Ignora Sempre', command=self._correggi, width=10
        ).grid(row=1, column=1, padx=5, pady=5, sticky=E)
        Button(
            fm_cmd, text='Aggiungi a diz.', command=self._correggi, width=10
        ).grid(row=1, column=2, padx=5, pady=5, sticky=E)
        fm_cmd.grid(row=0, column=1, padx=8, pady=8, sticky=EW)

        fm_hud.grid(row=1, column=0, padx=8, pady=8, sticky=EW)
        fm_hud.columnconfigure(0, weight=1)
        fm_hud.columnconfigure(1, weight=8)
        # ------------------------------------------------------

        fm_data = ttk.LabelFrame(self.root, text=" Contesto e Suggerimenti ")

        fm_txt = ttk.LabelFrame(fm_data, text=' Contesto ')
        self._txt = Text(fm_txt, width=77, height=12)
        self._txt.grid(row=0, column=1, padx=5, pady=5, sticky=EW)
        fm_txt.grid(row=0, column=0, padx=8, pady=8, sticky=EW)

        fm_hints = ttk.LabelFrame(fm_data, text=' Suggerimenti ')
        self._lbhints = Listbox(fm_hints, selectmode=SINGLE)
        self._lbhints.grid(row=0, column=1, padx=8, pady=8, sticky=EW)
        fm_hints.grid(row=0, column=1, padx=8, pady=8, sticky=EW, ipady=8)

        fm_data.grid(row=2, column=0, padx=8, pady=8, sticky=EW)
        fm_data.columnconfigure(0, weight=8)
        fm_data.columnconfigure(1, weight=1)
        # ------------------------------------------------------
        fm_save = ttk.LabelFrame(self.root, text=" Conferme ")
        Button(
            fm_save, text='Salva Modifiche', command=self._correggi, width=10
        ).grid(row=0, column=0, padx=5, pady=5, sticky=EW)
        fm_save.grid(row=3, column=0, padx=8, pady=8, sticky=EW)


        self.root.columnconfigure(0, weight=2)

    def _correggi(self):
        pass

    def _fill_hints(self, hints):
        for i in range(10):
            self._lbhints.insert(END, "hint n. " + str(i))

if __name__ == '__main__':
    root = Tk()
    gui = Gui(root)
    root.update_idletasks()
    root.mainloop()
