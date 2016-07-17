#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

address = re.compile(
    '''
    [\w\d.+-]+       # nome utente
    @
    ([\w\d.]+\.)+    # prefisso del nome di dominio
    (com|org|edu)    # dovremmo supportare più domini di livello più alto
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = address.search(candidate)
    if match:
        print '  Corrispondenza'
    else:
        print '  Nessuna corrispondenza'    