#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

address = re.compile(
    r'''

    # Il nome normale
    (?P<nome>\w+)
    \s+
    (([\w.]+)\s+)?      # Secondo nome opzionale o inizilae
    (?P<cognome>\w+)    # Cognome

    \s+

    <

    # Indirizzo: nome.cognome@domain.tld
    (?P<email>
      (?P=nome)
      \.
      (?P=cognome)      
      @
      ([\w\d.]+\.)+    # prefisso del nome di dominio
      (com|org|edu)    # limita i domini di livello più alto consentiti
    )

    >
    ''',
    re.UNICODE | re.VERBOSE | re.IGNORECASE)

candidates = [
    u'Nome Cognome <nome.cognome@example.com>',
    u'Diverso Nome <nome.cognome@example.com>',
    u'Nome SecondoNome Cognome <nome.cognome@example.com>',
    u'Nome S. Cognome <nome.cognome@example.com>',
    ]

for candidate in candidates:
    print
    print 'Candidato:', candidate
    match = address.search(candidate)
    if match:
        print '  Corrispondenza con nome :', match.groupdict()['nome'], match.groupdict()['cognome']
        print '  Corrispondenza con email:', match.groupdict()['email']    
    else:
        print '  Nessuna corrispondenza  :'
        