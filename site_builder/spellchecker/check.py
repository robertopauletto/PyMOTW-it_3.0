#!/usr/bin/env python
# -*- coding: utf-8 -*-
# check

__doc__ = """nuovo script"""
__version__ = "0.1"
__changelog__ = """

"""

import enchant


DEFAULT_LANGUAGE = "it_IT"

class SpellCheckerError(BaseException):
    pass


class SpellChecker():

    def __init__(self, language=None):
        """

        :param language:
        """
        self._lang = language or DEFAULT_LANGUAGE
        # if not enchant.dict_exists(self._lang):
        #     raise SpellCheckerError(
        #         "Dizionario {} non esistente".format(self._lang)
        #     )
        self.d = enchant.Dict(self._lang)

    def _check(self, word):
        """

        :param word:
        :return:
        """
        return self.d.check(word)

    def check_words(self, words):
        """(list of str) -> list of str

        Verifica ortografia elementi in `words'
        :param words:
        :return: gli elementi ortograficamente errati
        """
        errors = [word for word in words if not self._check(word)]
        return errors

    def check_with_suggestions(self, words):
        err_sugg = [(err, self.d.suggest(err))
                    for err in self.check_words(words)]
        return err_sugg
