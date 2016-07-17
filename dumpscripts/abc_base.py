#!/usr/binf/env python
# -*- coding: UTF-8 -*-

# abc_base.py

import abc


class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Recupera dati dalla sorgente in input e ritorna un oggetto"""

    @abc.abstractmethod
    def save(self, output, data):
        """Salva l'oggetto dati in output."""
