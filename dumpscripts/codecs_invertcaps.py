#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

def invertcaps(text):
    """Restituisce una nuova stringa con le lettere maiuscole trasformate
    in minuscole e viceversa.       
    """
    return ''.join( c.upper() if c in string.ascii_lowercase
                    else c.lower() if c in string.ascii_uppercase
                    else c
                    for c in text
                    )

if __name__ == '__main__':
    print invertcaps('ABC.def')
    print invertcaps('abc.DEF')
    