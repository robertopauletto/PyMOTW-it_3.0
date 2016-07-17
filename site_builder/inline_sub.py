#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Sostituzioni di stringhe specifiche con il corrispondente
codice html
Versione %s %s
""" % ( __version__, __date__ )

import string
from os.path import exists
from collections import defaultdict

DEFAULT_SUBS = [
    "sbk|<code>",
    "ebk|</code>",
    "sev|<span class='bkItem'>",
    "eev|</span>",
]

class InlineSubs(object):
    """
    Si occupa della sostituzione in linea di tag proprietari
    con le appropriate istruzioni html
    """
    def __init__(self, file_diz=None):
        """(str)

        Inizializza e carica gli elementi predefiniti nel
        dizionario di traduzione oppure gli elementi presenti nel file
        `file_diz`

        Prerequisito: `file_diz` contiene valori nel formato
        chiave|valore dove valore è un valido pezzo di codice html
        """
        self.diz = defaultdict(str)
        self.carica_diz(file_diz)

    def aggiungi_voce(self, chiave, valore):
        """(str, str)

        Incrementa il dizionario dei valori da sostituire
        """
        self.diz[chiave] = valore


    def carica_diz(self, file_diz):
        """([str])

        Carica le chiavi che restituiscono il codice html dal file
        `file_diz` se valorizzato oppure un insieme predefinito
        """
        if not file_diz or not exists(file_diz):
            to_parse = DEFAULT_SUBS
        else:
            to_parse = [riga.strip for riga in open(file_diz).readlines()
                        if riga and not riga.startswith("#")]

        for riga in to_parse:
            if not riga or riga.startswith("#"):
                continue
            chiave, valore = riga.strip().split('|')
            self.diz[chiave] = valore


    def rimpiazza(self, testo):
        """(str) -> str

        Ritorna la stringa modificata con il codice html
        """
        return string.Template(testo).safe_substitute(self.diz)




if __name__ == '__main__':
    print __doc__
    i = InlineSubs()
    import pprint
    pprint.pprint(i.diz)

