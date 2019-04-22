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
    """Caratteristiche dell'articolo sul modulo che saranno passate al
    template di DJango per il rendering"""
    fixed_sidebar = 20
    baseurl = 'examples'

    def __init__(self, indice, corpo, modulo, footer=Footer(), zipfile=None,
                 sidebar_is_fixed=True):
        """

        :param indice: contenuto della spalla destra (indice articolo)
        :param corpo: corpo dell'articolo
        :param modulo: info sul modulo
        :param footer:
        :param zipfile: file con gli esempi dell'articolo
        :param sidebar_is_fixed: se `True` la spalla destra è fissa
        """
        self._indice_sidebar = indice
        self._corpo = corpo
        self.modulo = modulo
        self.footer = footer
        self._zip = zipfile
        isinstance(self.modulo, Modulo)
        self._fixed_sidebar = sidebar_is_fixed

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
        return "fixed" if self._fixed_sidebar else "absolute"


if __name__ == '__main__':
    print(__doc__)
