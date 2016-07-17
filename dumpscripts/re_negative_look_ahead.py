#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

address = re.compile(
    '''
    ^

    # Un indirizzo: username@domain.tld

    # Ignora gli indirizzi noreply 
    (?!noreply@.*$)

    [\w\d.+-]+       # nome utente
    @
    ([\w\d.]+\.)+    # prefisso del nome di dominio
    (com|org|edu)    # limita i domini di livello più alto consentiti

    $
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'noreply@example.com',
    ]

for candidate in candidates:
    print
    print 'Candidato:', candidate
    match = address.search(candidate)
    if match:
        print '  Corrispondenza:', candidate[match.start():match.end()]
    else:
        print '  Nessuna corrispondenza'