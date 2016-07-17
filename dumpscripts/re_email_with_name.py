#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

address = re.compile(
    '''
    # Un nome è composto da lettere e può includere "." per titoli, 
    # abbreviazini ed iniziali intermedie
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+)
       \s*
       # Gli indirizzi email sono racchiusi tra parentesi angolari: < >
       # ma noi ne vogliamo solo uno se trovaiamo un nome, quindi 
       # mantenaimo la parentesi di partenza in questo gruppo
       <
    )? # l'intero nome è opzionalre

    # L'indirizzo email vero e proprio: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # nome utene
      @
      ([\w\d.]+\.)+    # prefisso del nome di dominio
      (com|org|edu)    # limita i domini di livello più alto consentiti
    )

    >? # parentesi angolare di chiusura opzionale
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'First Last',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
    u'<first.last@example.com>',
    ]

for candidate in candidates:
    print
    print 'Candidato:', candidate
    match = address.search(candidate)
    if match:
        print '  Nome corrisponde :', match.groupdict()['name']
        print '  email corrisponde:', match.groupdict()['email']
    else:
        print '  Nessuna corrispondenza'
        