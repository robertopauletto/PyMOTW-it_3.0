#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""
Integrazione di uno spell checker per il file .xml di traduzione
"""

try:
    from enchant.checker import SpellChecker
    from bs4 import BeautifulSoup
except ImportError as ierr:
    no_module = ierr.message.split()[-1]
    raise ImportError("E' richiesto il modulo " + no_module)


class EnchantProxy(object):
    
    def __init__(self, lang='it_IT'):
        self._lang = lang
        self._chrk = SpellChecker(lang)
        
class SpellCheck(object):
    """Contiene la logica per la verifica della sintassi del file xml di
    traduzione - viene verificato il testo contenuto nei tag definiti nella
    variabile di classe tags_to_check"""
    tags_to_check = ['testo_normale', 'note']

    def __init__(self, to_check):
        """Ottiene il testo da verificare"""
        self._soup = BeautifulSoup(to_check, "lxml")
        self._ep = EnchantProxy()
        self._chunks = self._get_chunks()

    def _get_chunks(self):
        """Estrae gli elementi da verificare specificati in tags_to_check"""
        retval = []
        for tag in SpellCheck.tags_to_check:
            retval.extend(self._soup.findAll(tag))
        return retval

    def get_checked(self, is_prettyprinted=False):
        """([bool]) -> str

        Ritorna il testo corretto"""
        return str(self._soup) if not is_prettyprinted \
            else self._soup.prettify()

