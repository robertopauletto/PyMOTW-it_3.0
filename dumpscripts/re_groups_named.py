#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'
print text
print 

for pattern in [ r'^(?P<prima_parola>\w+)',
                 r'(?P<ultima_parola>\w+)\S*$',
                 r'(?P<parola_t>\bt\w+)\W+(?P<altra_parola>\w+)',
                 r'(?P<finisce_con_o>\w+o)\b',
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print 'Corrispondenza "%s"' % pattern
    print '  ', match.groups()
    print '  ', match.groupdict()
    print