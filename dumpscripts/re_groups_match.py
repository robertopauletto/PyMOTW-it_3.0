#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'

print text
print

for pattern in [ r'^(\w+)',          # parola ad inizio stringa
                 r'(\w+)\S*$',        # parola a fine stringa, with punteggiatura opzionale
                 r'(\bt\w+)\W+(\w+)', # parola che inizia con 't' poi un'altra parola
                 r'(\w+o)\b',         # parola che finisce con 'o'
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print 'Corrispondenza: "%s"' % pattern
    print '  ', match.groups()
    print