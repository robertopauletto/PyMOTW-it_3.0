#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def my_function(a, b):
    """Ritorna a * b.

    >>> my_function(['A', 'B', 'C'], 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B', 'C',
     'A', 'B', 'C',
     'A', 'B', 'C']

    Questo non corrisponde perchè c'è uno spazio extra dopo la [ nella lista
    
    >>> my_function(['A', 'B', 'C'], 2) #doctest: +NORMALIZE_WHITESPACE
    [ 'A', 'B', 'C',
      'A', 'B', 'C' ]
    """
    return a * b

