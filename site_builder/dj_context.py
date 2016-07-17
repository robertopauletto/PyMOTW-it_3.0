#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Costruisce le pagine indice
Versione %s %s
""" % ( __version__, __date__ )


class DjContext(object):
    """
    Rappresenta una classe astratta da utilizzare per ottenere un
    oggetto Context
    """
    
    def get_context(self):
        raise NotImplemented()