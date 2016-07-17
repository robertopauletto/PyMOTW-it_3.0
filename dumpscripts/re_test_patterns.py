#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re

def test_patterns(text, patterns=[]):
    """Dato un testo sorgente ed un elenco di modelli, cerca 
    corrispondenze per ogni modello all'interno del testo e le 
    stampa a stdout
    """
    # Mostra la posizione dei caratteri ed il testo in input
    print
    print ''.join(str(i/10 or ' ') for i in range(len(text)))
    print ''.join(str(i%10) for i in range(len(text)))
    print text

    # Cerca le corrispondenze per ogni modello nel testo e stampa i risultati
    for pattern in patterns:
        print
        print 'Corrispondenza con "%s"' % pattern
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print '  %2d : %2d = "%s"' % \
                (s, e-1, text[s:e])
    return

if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa', ['ab'])