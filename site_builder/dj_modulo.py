#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""
Versione %s %s
""" % ( __version__, __date__ )

from modulo import Modulo
from footer import Footer
import os.path

class DjModulo(object):
    fixed_sidebar = 20
    baseurl = 'examples'
    def __init__(self, indice, corpo, modulo, footer=Footer(), zipfile=None):
        self._indice_sidebar = indice
        self._corpo = corpo
        self.modulo = modulo
        self.footer = footer
        self._zip = zipfile
        isinstance(self.modulo, Modulo)


    @property
    def lnkzip(self):
        if not self._zip:
            return None
        return os.path.join(DjModulo.baseurl, os.path.basename(self._zip))

    @property
    def titolo(self):
        x = " - ".join((self.modulo.nome, self.modulo.titolo))
        x = x.replace('_', ' ')
        if self.modulo.nome == "os":
            return "os - Accesso portabile alle funzionalit&agrave; specifiche di un sistema operativo"
        return x
    
    @property
    def descrizione(self):
        if self.modulo.nome == "os":
            return "Accesso portabile alle funzionalit&agrave; specifiche di un sistema operativo"
        return self.modulo.descrizione
    
    @property
    def versione(self):
        return self.modulo.versione
    
    @property
    def indice_laterale(self):
        return self._indice_sidebar

    @property
    def main_content(self):
        try:
            tmp = "\n".join(self._corpo)
        except Exception as err:
            print(err)
            return "Errore: ", err.message
        return tmp

    @property
    def sidebarnav_type(self):
        return "fixed" if len(self.indice_laterale) <= DjModulo.fixed_sidebar \
            else "absolute"


if __name__ == '__main__':
    print(__doc__)
