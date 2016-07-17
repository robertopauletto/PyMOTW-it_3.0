#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def double_space(lines):
    """Stampa un elenco di righe con doppia spaziatura

    >>> double_space(['Riga uno.', 'Riga due.'])
    Riga uno.
    
    Riga due.
    
    """
    for l in lines:
        print l
        print
    return
