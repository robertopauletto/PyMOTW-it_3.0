#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns('Ecco una porzione di testo -- contiene punteggiatura.',
              [ r'^\w+',     # parola ad inizio stringa
                r'\A\w+',    # parola ad inizio stringa
                r'\w+\S*$',  # parola alla fine della stringa, con punteggiatura opzionale
                r'\w+\S*\Z', # parola alla fine della stringa, con punteggiatura opzionale
                r'\w*t\w*',  # parola che contiene 't'
                r'\bt\w+',   # 't' ad inizio parola
                r'\w+e\b',   # 'e' alla fine della parola
                r'\Bt\B',    # 't', non inizia o finisce in una parola
                ])
