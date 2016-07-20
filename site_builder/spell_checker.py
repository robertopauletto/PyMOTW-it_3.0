#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__='2016-07-17'
__version__='0.1'
__doc__="""
Integrazione di uno spell checker per il file .xml di traduzione
"""

try:
    from enchant import DictWithPWL
    from enchant.checker import SpellChecker
    from enchant.tokenize import URLFilter, EmailFilter
    import enchant.errors
    from collections import namedtuple
    from bs4 import BeautifulSoup
except ImportError as ierr:
    no_module = ierr.message.split()[-1]
    raise ImportError("E' richiesto il modulo " + no_module)

class SpellCheckError(Exception):
    pass

class EnchantProxy(object):
    """Wrapper alla libreria enchant"""
    def __init__(self, mydict=None, lang='it_IT'):
        """[str]

        Ottiene l'eventuale elenco di parole personalizzate da integrare al
        dizionario ed il linguaggio da applicare - predefinito Italiano
        """
        self._lang = lang
        try:
            self._chkr = SpellChecker(lang, filters=[EmailFilter, URLFilter])
            self._pwl = DictWithPWL(lang, mydict) if mydict else None
        except enchant.errors.DictNotFoundError as nodict_err:
            raise SpellCheckError("Dizionario " + lang + " non trovato")

    def check(self, text):
        """(str) -> list of tuples

        Esegue il controllo per ``testo`` e ritorna una lista di oggetti
        ``Errore`` con la parola errata e la lista dei suggerimenti.
        Se la parola non viene trovata viene effettuata una ricerca anche nel
        dizionario personale (``self._pwl``) se definito
        """
        errors = []
        self._chkr.set_text(text)
        for err in self._chkr:
            if self._pwl and self._pwl.check(err.word):
                continue
            errors.append(Errore(err.word, self._chkr.suggest(err.word)))
        return errors

    def upd_mydict(self, word):
        """(str)

        Aggiunge ``word`` al dizionario personalizzato (attiva per la
        prossima chiamata a ``check``
        """
        if not self._pwl:
            return
        self._pwl.add(word)

# Namedtuple che contiene la parola errata e la lista dei suggerimenti
Errore = namedtuple('errore', 'parola sugg')


class SpellCheck(object):
    """Contiene la logica per la verifica della sintassi del file xml di
    traduzione - viene verificato il testo contenuto nei tag definiti nella
    variabile di classe tags_to_check"""
    tags_to_check = ['testo_normale', 'note']

    def __init__(self, to_check, mywords=None):
        """Ottiene il testo da verificare"""
        self._soup = BeautifulSoup(to_check, "lxml")
        self._ep = EnchantProxy(mydict=mywords)
        self._chunks = self._get_chunks()

    def _get_chunks(self):
        """Estrae gli elementi da verificare specificati in tags_to_check"""
        retval = []
        for tag in SpellCheck.tags_to_check:
            retval.extend(self._soup.findAll(tag))
        return retval

    def get_checked(self, prettyprinted=False):
        """([bool]) -> str

        Ritorna il testo corretto, se ``prettyprinted`` ritorna il testo
        formattato"""
        return str(self._soup) if not prettyprinted else self._soup.prettify()

    def check(self):
        """Temporanea per debug visualizza le parole errate ed i suggerimenti"""
        self._ep.upd_mydict('Twister')
        for chunk in self._chunks:
            errori = self._ep.check(chunk.text)
            if not errori:
                continue
            print "\n".join(
                [err.parola + " " + ' '.join(err.sugg) for err in errori]
            )
            raw_input("Premi enter per il prossimo controllo")

if __name__ == '__main__':
    testfile = "/home/robby/random.xml"
    mywords = "/home/robby/ownCloud/spell_mywords.txt"
    import codecs
    sc = SpellCheck(codecs.open(testfile, encoding='utf-8'), mywords)
    sc.check()

