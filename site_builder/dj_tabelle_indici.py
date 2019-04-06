#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Costruisce le pagine indice
Versione %s %s
""" % ( __version__, __date__ )

from collections import OrderedDict
import datetime
from modulo import Modulo

class DjTabelleIndici(object):
    base_url = 'indice.html'
    """
    Rappresenta una pagina che contiene una tabella con l'indice dei moduli
    """
    def __init__(self, moduli, footer):
        """(list of :py:class:Modulo, :py:class:`Footer`)"""
        self._moduli = moduli
        self.footer = footer

    @property
    def elenco_moduli(self):
        """() -> list of `:py:class:Modulo`
        Ritorna un elenco di oggetti `:py:class:Modulo` ordinati per
        nomi
        """
        return sorted(self._moduli, key=lambda x:x.nome.lower())
    
    @property
    def last_upd(self):
        return datetime.date.today().strftime("%d.%m.%Y") 

    @property
    def get_indice(self):
        diz = OrderedDict()
        moduli = self.elenco_moduli
        for i in range(65, 91):
            letter = chr(i)
            if letter in diz:
                continue
            aref = [modulo.nome for modulo in moduli
                    if modulo.nome.upper().startswith(letter)]
            diz[letter] = aref[0] if aref else None
        return diz

    
if __name__ == '__main__':
    pass
