#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'
import re

def test_patterns(text, patterns=[]):
    """Dato un testo sorgente ed un elenco di modelli
    cerca corrispondenze per ogni modello all'interno del testo
    e le stampa su stdout.
    """
    # Mostra la posizione del carattere ed il testo in input
    print
    print ''.join(str(i/10 or ' ') for i in range(len(text)))
    print ''.join(str(i%10) for i in range(len(text)))
    print text

    # Cerca corrispondenza nel testo per ogni modello
    # e stampa i risultati1
    for pattern in patterns:
        print
        print 'Cerco corrispondenze ... "%s"' % pattern
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print '  %2d : %2d = "%s"' % \
                (s, e-1, text[s:e])
            print '    Grouppi:', match.groups()
            if match.groupdict():
                print '    Gruppi con intestazione:', match.groupdict()
            print
    return