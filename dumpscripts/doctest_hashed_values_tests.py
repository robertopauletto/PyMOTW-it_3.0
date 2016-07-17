#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def group_by_length(words):
    """Ritorna un dizionario che raggruppa le parole in insiemi omogenei per lunghezza

    >>> grouped = group_by_length([ 'python', 'modulo', 'della', 'il', 'settimana' ])
    >>> grouped == { 5:set(['della']),
    ...              2:set(['il']),
    ...              9:set(['settimana']),
    ...              6:set(['python', 'modulo']),
    ...              }
    True

    """
    d = {}
    for word in words:
        s = d.setdefault(len(word), set())
        s.add(word)
    return d
