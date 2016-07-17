#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__='02/11/2013'
__version__='2.0'

__doc__ = """
Versione %s %s
""" % ( __version__, __date__ )


import os.path
import codecs
import traceback
import re
from functools import partial
from django.utils.encoding import smart_text
import my_html

h = my_html.MyHtml()  # Si occupa del rendering in HTML dei dati

DEF_CHARSET='utf-8'

def ottieni_tabella(elenco_moduli):
    """(list of `:py:class:Modulo`)
    
    """
    retval = []
    for modulo in elenco_moduli:
        retval.append(modulo.per_tabella_indice())
    return h.table(retval, False)