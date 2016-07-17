#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""
Spell checker
"""

try:
    from enchant.checker import SpellChecker
except:
    raise ImportError("E' richiesto il modulo enchant")

class EnchantProxy(object):
    
    def __init__(self, lang='it_IT'):
        self._lang = lang
        self._chrk = SpellChecker(lang)
        
    
        