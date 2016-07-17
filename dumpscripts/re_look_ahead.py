#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

address = re.compile(
    '''
    # Un nome è composto da lettere, e può comprendere "." per abbreviazioni
    # ed iniziali del secondo nome
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+
     )
     \s+
    ) # name non è più opzionale

    # LOOKAHEAD
    # Gli indirizzi email sono incorporati in parentesi angolari, ma si 
    # vogliono le parentesi sono se sono presenti entrambe, oppure nessuna.
    (?= (<.*>$)       # il resto è racchiuso tra parentesi angolari
        |
        ([^<].*[^>]$) # il resto *non* è racchiuso tra parentesi angolari
      )

    <? # parentesi angolare aperta opzionale

    # L'indirizzo vero e proprio: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # nome utente
      @
      ([\w\d.]+\.)+    # prefisso del nome di dominio
      (com|org|edu)    # limita i domini di livello più alto consentiti
    )

    >? # parentesi angolare chiusa opzionale
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'Nome Cognome <first.last@example.com>',
    u'No Parentesi first.last@example.com',
    u'Parentesi aperta <first.last@example.com',
    u'Parentesi Chiusa first.last@example.com>',
    ]

for candidate in candidates:
    print
    print 'Candidatp:', candidate
    match = address.search(candidate)
    if match:
        print '  Corrispondenza con il nome :', match.groupdict()['name']
        print '  Corrispondenza con email   :', match.groupdict()['email']
    else:
        print '  Nessuna corrispondenza'