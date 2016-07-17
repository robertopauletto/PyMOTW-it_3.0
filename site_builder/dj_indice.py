#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Costruisce le pagine indice
Versione %s %s
""" % ( __version__, __date__ )

from modulo import Modulo
import datetime

class Indice(object):
    base_url = 'index%s.html'
    moduli_per_riga = 3
    """
    Rappresenta una pagina indice con elenco moduli in ordine
    cronologicamente decrescente
    """
    def __init__(self, elenco_moduli, footer, categ, nr_pagina=None):
        """(list of :py:class:Modulo, :py:class:`Footer` [,int])"""
        assert len(elenco_moduli) < 13  # 12 moduli per pagina
        self.moduli = elenco_moduli
        self._ind_s = 0
        self._ind_e = 0
        self._retind = 0
        self.prev_nr_page = -1
        self.next_nr_page = -1
        self.footer = footer
        self.elenco_categorie = categ



    @property
    def prev_url(self):
        if self.prev_nr_page >= 0:
            return Indice.base_url % ("_" + str(self.prev_nr_page))
        else:
            return Indice.base_url % ''

    @property
    def next_url(self):
        if self.next_nr_page > 0:
            return Indice.base_url % ("_" + str(self.next_nr_page))
        else:
            return Indice.base_url % ''

        
    @property
    def modulo_tre(self):
        """
        Ottiene una lista composta da liste di 3 oggetti
        `py:class:Modulo`
        """
        return [self.moduli[i:i+Indice.moduli_per_riga]
             for i in range(0, len(self.moduli), Indice.moduli_per_riga)]
        
    
    
if __name__ == '__main__':
    pass