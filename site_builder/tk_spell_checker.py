#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__='2016-07-20'
__version__='0.1'
__doc__="""
Interfaccia grafica per lo spell check di un articolo tradotto
"""

import codecs
from Tkinter import *
import ttk
from tkFileDialog import askopenfilename
from tkMessageBox import askokcancel, askquestion, askyesno
from tkMessageBox import showerror, showinfo
from shutil import copy
import os.path
import datetime
import spell_checker


INIT_DIR = '../tran'
INIT_DIR = '/home/robby'
MYDICT = "/home/robby/ownCloud/spell_mywords.txt"


class ContatoreErrori(object):
    """Rappresenta un riepilogo per tipologia di una collezione di `Error`"""
    def __init__(self, errors):
        """(list of Error)

        Ottiene una lista di oggetti Error
        """
        self._errors = errors
        self._ign = 0
        self._chkd = 0
        self._cust = 0
        self._tot = len(errors)

    @property
    def custom(self):
        """Numero di errori corretti aggiungendo la parola errata al dizionario
        personalizzato
        """
        return self._cust

    @property
    def ignored(self):
        """Numero di errori da ignorare"""
        return self._ign

    @property
    def checked(self):
        """Numero di errori verificati"""
        return self._chkd

    @property
    def tot(self):
        """NUmero di errori totali"""
        return self._tot

    @property
    def togo(self):
        """Numero di errori ancora da elaborare"""
        return self.tot - self.ignored - self.checked - self.custom

    def conta(self):
        """Ritorna una riepilogo per tipologia"""
        z = [e for e in self._errors if e.is_customized_word]
        self._cust = len([e for e in self._errors if e.is_customized_word])
        self._ign = len([e for e in self._errors if e.is_ignored_word])
        self._chckd = len([e for e in self._errors if e.correct_word])


class Gui(object):
    """Interfaccia grafica per la gestione degli errori """
    def __init__(self, root, geometry="800x600+100+200"):

        self._pos = 0
        self._sc = None
        self._txt = None
        self._lbhints = None
        self.root = root
        self.root.title("Correttore Ortografico")
        self.root.wm_iconbitmap('@spell_checking.xbm')
        if geometry:
            self.root.geometry(geometry)
        self._file = StringVar(value='Scegliere il file da correggere')
        self._new_word = StringVar()
        self._err_word = StringVar()
        self._chk_pprint = StringVar(value='0')
        self._chk_backup = StringVar(value='1')
        self._statusbar = StatusBar(self.root, 4)
        self._statusbar.set_text(" " * 40, 0)
        self._statusbar.set_text("   ", 1)
        self._statusbar.set_text("   ", 2)
        self._statusbar.set_text("   ", 3)
        self._contaerr = None  # Contatore errori
        self._position = StringVar(value='-')
        self._draw()

    def _draw(self):
        """Disegno dell'interfaccia"""
        fm = ttk.LabelFrame(self.root, text=" File da tradurre ")
        Entry(
            fm, textvariable=self._file
        ).grid(row=0, column=0, padx=5, pady=5, sticky=EW)
        Button(
            fm, text='Sfoglia', command=self._sfoglia
        ).grid(row=0, column=1, padx=5, pady=5, sticky=EW)
        fm.columnconfigure(0, weight=2)
        fm.grid(row=0, column=0, padx=8, pady=8, sticky=EW)

        # ------------------------------------------------------

        fm_hud = ttk.LabelFrame(self.root, text=" Comandi e Navigazione ")

        fm_nv = ttk.LabelFrame(fm_hud, text=' Navigazione ')
        Button(
            fm_nv, text='<<', width=5, command=lambda: self._nav_errors('rw')
        ).grid(row=0, column=0, padx=5, pady=5)
        Button(
            fm_nv, text='<', command=lambda: self._nav_errors('prev'), width=5
        ).grid(row=0, column=1, padx=5, pady=5)
        Button(
            fm_nv, text='>', command=lambda: self._nav_errors('next'), width=5
        ).grid(row=0, column=2, padx=5, pady=5)
        Button(
            fm_nv, text='>>', width=5, command=lambda: self._nav_errors('ff')
        ).grid(row=0, column=3, padx=5, pady=5)
        Label(
            fm_nv, text="Errore n. "
        ).grid(row=1, column=0,  padx=5, pady=5)
        Label(
            fm_nv, textvariable=self._position, justify=LEFT, anchor=W
        ).grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        fm_nv.grid(row=0, column=0, ipady=5)

        # ------------------------------------------------------

        fm_cmd = ttk.LabelFrame(fm_hud, text=' Comandi ')
        Entry(
            fm_cmd, width=20, textvariable=self._new_word
        ).grid(row=0, column=0, padx=5, pady=5)
        Entry(
            fm_cmd, width=20, textvariable=self._err_word, state=DISABLED
        ).grid(row=1, column=0, padx=5, pady=5)
        Button(
            fm_cmd, text='Correggi', command=self._correggi, width=10
        ).grid(row=0, column=1, padx=5, pady=5)
        Button(
            fm_cmd, text='Ignora',
            command=lambda: self._ignora(True), width=10
        ).grid(row=0, column=2, padx=5, pady=5)
        Button(
            fm_cmd, text='Ignora Sempre', width=10,
            command=lambda: self._ignora(False)
        ).grid(row=1, column=1, padx=5, pady=5, sticky=E)
        Button(
            fm_cmd, text='Aggiungi a diz.', command=self._custom_word, width=10
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
        self._lbhints.bind('<<ListboxSelect>>', self._onlbselect)
        self._lbhints.grid(row=0, column=1, padx=8, pady=8, sticky=EW)
        fm_hints.grid(row=0, column=1, padx=8, pady=8, sticky=EW, ipady=8)

        fm_data.grid(row=2, column=0, padx=8, pady=8, sticky=EW)
        fm_data.columnconfigure(0, weight=8)
        fm_data.columnconfigure(1, weight=1)
        # ------------------------------------------------------
        fm_save = ttk.LabelFrame(self.root, text=" Conferme ")
        Button(
            fm_save, text='Salva Modifiche', command=self._salva, width=10
        ).grid(row=0, column=0, padx=5, pady=5, sticky=EW)
        ttk.Checkbutton(
            fm_save, text='Formatta', variable=self._chk_pprint
        ).grid(row=0, column=1, padx=5, pady=5, sticky=EW)
        ttk.Checkbutton(
            fm_save, text='Salva Originale', variable=self._chk_backup
        ).grid(row=0, column=2, padx=5, pady=5, sticky=EW)

        fm_save.grid(row=3, column=0, padx=8, pady=8, sticky=EW)

        self.root.columnconfigure(0, weight=20)
        self._statusbar.grid(row=99, column=0, sticky=EW, padx=8, pady=8)

    def _conferma_salvataggio(self):
        """"""
        prompt = ["Confermi salvataggio di %s" % self._file.get()]
        prompt.append(
            "%s formattazione del file?" % "con"
            if int(self._chk_pprint.get()) else "senza"
        )
        prompt.append("%s file originale" % (
            "effettuando una copia del " if self._chk_backup.get() else
            "sovrascrivendo il "
        ))
        return askokcancel("Salvataggio", "\n".join(prompt))

    def _get_bk_filename(self):
        folder, fn = os.path.split(self._file.get())
        fn, ext = os.path.splitext(fn)
        ts = datetime.datetime.now().strftime("-%Y%m%d-%H%M%S")
        return os.path.join(folder, fn + ts + ext)

    def _salva(self):
        if not self._sc:
            showinfo("Salvataggio", "Prima selezionare un file da correggere")
            return
        if not self._conferma_salvataggio():
            return
        or_file = self._file.get()
        bk_file = self._get_bk_filename() if self._chk_backup.get() else ""
        copy(or_file, bk_file)
        pp = bool(int(self._chk_pprint.get()))
        text = self._sc.get_checked(pp)
        self._sc.add_custom_words()
        codecs.open(or_file, mode='w', encoding="utf-8").write(text)
        self._statusbar.set_text(bk_file, 1)
        showinfo("Salvataggio", "Salvataggio eseguito")

    def _onlbselect(self, event):
        """Istanzia ``_new_word`` con il suggerimento selezionato nel listbox"""
        w = self._lbhints.curselection()
        if w:
            self._new_word.set(self._lbhints.get(w))

    def _correggi(self):
        """Imposta la nuova parola nell'oggetto Error selezionato"""
        if not self._new_word.get():
            return
        new_word = self._new_word.get()
        err_word = self._err_word.get()
        for error in self._sc.errors:
            if error.err_word == err_word:
                self._sc.errors[self._pos].correct_word = new_word
                print "Corretta ", error.idx, new_word

    def _ignora(self, single=False):
        """Appone il contrassegno di errore da ignorare per
        l'errore selezionato
        """
        if single:
            self._sc.errors[self._pos].ignore_word()
            return
        word = self._sc.errors[self._pos].err_word
        for error in self._sc.errors:
            if not error.err_word == word:
                continue
            error.ignore_word()
            print "Ignorata ", error.idx, word
        self._show_status_errors()

    def _custom_word(self):
        """Appone il contrassegno di parola da aggiungere al dizionario
        personalizzato
        """
        word = self._err_word.get()
        for error in self._sc.errors:
            if not error.err_word == word:
                continue
            print "Personalizzata ", error.idx, word
            error.add_to_dict(word)

    def _sfoglia(self):
        """Ottiene il nome del file .xml da elaborare e passa il contenuto
        del file allo spell checker
        """
        ft = [("File xml", "*.xml")]
        tran_file = askopenfilename(
            initialdir=INIT_DIR,
            filetypes=ft,
            parent=self.root,
            title='Scegliere il file di traduzione da correggere'
        )
        if not os.path.exists(tran_file):
            showerror(
                title='Scelta file', msg='File non esiste o non selezionato'
            )
            return
        self._file.set(tran_file)
        text = codecs.open(tran_file, encoding="utf-8")
        self._sc = spell_checker.SpellCheck(text, MYDICT)
        self._sc.check()
        self._show_error()
        self._position.set(self._pos +1)
        self._contaerr = ContatoreErrori(self._sc.errors)
        self._show_status_errors()

    def _show_error(self):
        """Mostra la parola errata, il contesto in cui appare ed i
        suggerimenti
        """
        error = self._sc.errors[self._pos]
        isinstance(error, spell_checker.Error)
        self._err_word.set(error.err_word)
        self._new_word.set("")
        self._fill_hints(error.hints)
        isinstance(self._txt, Text)
        self._txt.delete(1.0, END)
        self._txt.insert(1.0, error.context)


    def _check_errors_to_go(self):
        """Verifica se nella collezione di Error ce ne sono ancora da
        esaminare e ne ritorna il numero
        """
        pass

    def _show_status_errors(self):
        """Visualizza lo stato della collezione di errori da gestire"""
        self._contaerr.conta()
        self._statusbar.set_text(
            "%d / %d errori da correggere/rilevati" % (
                 self._contaerr.togo, self._contaerr.tot
            ), 0
        )
        self._statusbar.set_text(
            "%d errori corretti" % self._contaerr.checked, 1
        )
        self._statusbar.set_text(
            "%d errori ignorati" % self._contaerr.ignored, 2
        )
        self._statusbar.set_text(
            "%d parole personalizzate" % self._contaerr.custom, 3
        )

    def _nav_errors(self, goto):
        """Imposta il puntatore della sequenza degli errori da elaborare in
        base alla scelta di navigazione dell'utente e mostra l'errore
        corrispondente

        ``goto`` è una parola chiave che indica il tipo di spostamento:
        - next -> errore successivo (se fine sequenza va al primo)
        - prev -> errore precedente (se inizio sequenza va all'ultimo)
        - ff -> all'ultimo errore della sequenza
        - rw -> al primo errore della sequenza
        """
        if not self._sc.errors:
            return
        goto = goto.lower()
        if not goto in ['next', 'prev', 'ff', 'rw']:
            showerror("Navigazione", "Tipo di spostamento non riconosciuto")
            return
        if goto == 'next':
            self._pos += 1
            while self._sc._errors[self._pos].is_checked:
                self._pos += 1
                if self._pos == len(self._sc.errors):
                    showinfo("", "Fine archivio")
                    self._pos -=1
                    break
        elif goto == 'prev':
            self._pos -=1
            while self._sc._errors[self._pos].is_checked:
                if self._pos < 0:
                    showinfo("", "Inizio archivio")
                    self._pos +=1
                    break
        elif goto == 'ff':
            self._pos = len(self._sc.errors) - 1
            while self._sc._errors[self._pos].is_checked:
                self._pos -= 1
        elif goto == 'rw':
            self._pos = 0
            while self._sc._errors[self._pos].is_checked:
                self._pos += 1

        self._show_error()
        self._show_status_errors()
        self._position.set(self._pos +1)

    def _fill_hints(self, hints):
        """Riempie il listbox dei suggerimenti per l'errore selezionato"""
        self._lbhints.delete(0, END)
        for hint in hints:
            self._lbhints.insert(END, hint)


class StatusBar(Frame):
    """Rappresenta una barra di stato"""
    def __init__(self, master, labels=1):
        """``labels`` è il numero di etichette di stato da visualizzare"""
        Frame.__init__(self, master)
        self._svars = []
        for i in range(labels):
            self._svars.append(StringVar(value=''))
            Label(
                self, textvariable=self._svars[i], relief=SUNKEN
            ).grid(row=0, column=i,  sticky=EW, padx=5, pady=5)
        self.columnconfigure(0, weight=5)

    def set_text(self, text, index):
        """Assegna ``text`` all'etichetta identificata da ``index``"""
        self._svars[index].set(text)
        self.update_idletasks()


if __name__ == '__main__':
    root = Tk()
    gui = Gui(root)
    root.update_idletasks()
    root.mainloop()
