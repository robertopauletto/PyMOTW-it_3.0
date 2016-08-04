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
        self._custom_dict = mydict
        try:
            self._chkr = SpellChecker(lang, filters=[EmailFilter, URLFilter])
            self._pwl = DictWithPWL(lang, mydict) if mydict else None
        except enchant.errors.DictNotFoundError as nodict_err:
            raise SpellCheckError("Dizionario " + lang + " non trovato")

    def check(self, text, chunk_idx):
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
            error = Error(err.word, self._chkr.suggest(err.word), chunk_idx)
            error.context = text
            errors.append(error)
        return errors

    def upd_mydict(self, word):
        """(str)

        Aggiunge ``word`` al dizionario personalizzato (attiva per la
        prossima chiamata a ``check``
        """
        if not self._pwl:
            return
        self._pwl.add(word)

    def add_custom_word(self, words):
        """(list of str)

        Aggiunge le parole in ``words`` al dizionario personalizzato
        """
        if not self._custom_dict:
            raise SpellCheckError("Dizionario personalizzato non presente")
        orig_words = codecs.open(self._custom_dict, encoding='utf-8').split("\n")
        orig_words.extend([w for w in words if w not in orig_words])
        codecs.open(
            self._custom_dict, mode='w', encoding='utf-8'
        ).write("\n".join(orig_words))

class Error(object):
    """Rappresenta una parola ortograficamente non corretta oppure non
    compresa nel dizionario"""
    def __init__(self, word, hints, chunk_idx):
        """(str, list of str

        Imposta la parola errata ed i suggerimenti.
        ``chunk_idx`` è il progressivo di lista nel quale si trova il testo
        a cui appartiene l'errore nel file di traduzione; servirà poi per
        ricostruire il flusso di traduzione con le modifiche utente
        """
        self._word = word
        self._hints = hints
        self._replacement = None
        self._add_to_dict = False
        self._context = ""
        self._chunk_idx = chunk_idx
        self._ignore = False

    @property
    def is_checked(self):
        """Ritorna ``True`` se l'errore non è già stato trattato, vale a dire
        se ``_ignore`` è ``False`` oppure se ``_add_to_dict è ``False``
        oppure se `_replacement`` è `None``"""
        if self._replacement:
            return True
        if self._add_to_dict:
            return True
        if self._ignore:
            return True
        return False

    @property
    def replacement(self):
        return self._replacement

    @property
    def idx(self):
        return self._chunk_idx

    @property
    def hints(self):
        """Ritorna una lista di suggerimenti per la parola errata"""
        return self._hints

    @property
    def is_ignored_word(self):
        """Se true l'errore deve essere ignorato ignorato"""
        return self._ignore

    @property
    def context(self):
        """Ottiene il contesto di appartenenza dell'errore"""
        return self._context

    @context.setter
    def context(self, text):
        """Ottiene il contesto di appartenenza dell'errore"""
        self._context = text

    @property
    def err_word(self):
        """Ottiene la parola errata"""
        return self._word

    @property
    def correct_word(self):
        """Ottiene la parola corretta"""
        return self._replacement

    @correct_word.setter
    def correct_word(self, word):
        """Imposta la parola corretta"""
        self._replacement = word

    @property
    def is_customized_word(self):
        """Se la parola è da aggiungere al diz. personalizzato ritorna True"""
        return self._add_to_dict

    def ignore_word(self):
        """Se true l'errore è ignorato"""
        self._ignore = True

    def add_to_dict(self, word):
        """(str)

        Imposta a true ``_add_to_dict`` ed inserisce la parola da aggiungere
        al dizionario in ``_word``
        """
        self._add_to_dict = True
        self._replacement = word

    @staticmethod
    def get_custom_words(errors):
        """(list of Errori) -> list of str

        Itera su ``errors`` e ritorna una lista delle parole che sono state
        marcate come da aggiungere al dizionario personalizzato,
        """
        return [e._word for e in errors if e._add_to_dict]

    @staticmethod
    def remove_words(errors, words):
        """(list of Error, list of str) -> list of Error

        Itera su errors e rimuove la cui parola errata è contenuta in ``words``
        """
        new_err = [e for e in errors if e.err_word in words]
        return new_err


class SpellCheck(object):
    """Contiene la logica per la verifica della sintassi del file xml di
    traduzione - viene verificato il testo contenuto nei tag definiti nella
    variabile di classe tags_to_check"""
    tags_to_check = ['testo_normale', 'note']

    def __init__(self, to_check, mywords=None):
        """Ottiene il testo da verificare
        
        """
        self._soup = BeautifulSoup(to_check, "lxml")
        self._ep = EnchantProxy(mydict=mywords)
        self._chunks = self._get_chunks()
        self._errors = []

    @property
    def errors(self):
        return self._errors

    def _correct_chunks(self):
        for error in self._errors:
            isinstance(error, Error)
            if error.replacement:
                self._chunks[error.idx].string.replace(
                    error.err_word, error.replacement
                )



    def add_custom_words(self):
        pass

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
        """Itera sul testo da verificare ed istanzia un elenco di oggetti
        ``Error`` da elaborare
        """
        for i, chunk in enumerate(self._chunks):
            error = self._ep.check(chunk.text, i)
            if not error:
                continue
            self._errors.extend(error)

    def tmpcheck(self):
        """Temporanea per debug visualizza le parole errate ed i suggerimenti"""
        self._ep.upd_mydict('Twister')
        for i, chunk in enumerate(self._chunks):
            errori = self._ep.check(chunk.text, i)
            if not errori:
                continue
            print "\n".join(
                [err._word + " " + ' '.join(err._hints) for err in errori]
            )
            raw_input("Premi enter per il prossimo controllo")

if __name__ == '__main__':
    testfile = "/home/robby/random.xml"
    mywords = "/home/robby/ownCloud/spell_mywords.txt"
    import codecs
    sc = SpellCheck(codecs.open(testfile, encoding='utf-8'), mywords)
#    sc.tmpcheck()

