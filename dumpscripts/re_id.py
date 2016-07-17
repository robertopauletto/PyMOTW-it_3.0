#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import re

address = re.compile(
    '''
    ^

    # Un nome è composto da lettere, e può comprendere "." per abbreviazioni
    # di titoli ed iniziali di secondo nome
    (?P<nome>
       ([\w.]+\s+)*[\w.]+
     )?
    \s*

    # Gli indirizzi email sono racchiusi tra parentesi angolari, ma vogliamo
    # le parentesi solo se troviamo un nome
    (?(nome)
      # visto che abbiamo un nome il resto è racchiuso tra parentesi angolari
      (?P<parentesi>(?=(<.*>$)))
      |
      # non abbiamo un nome ed il resto non deve comprendere parentesi angolari
      (?=([^<].*[^>]$))
     )

    # Cerchiamo le parentesi angolari solo se l'asserzione look ahead le ha 
    # trovate entrambe
    (?(parentesi)<|\s*)

    # Indirizzo: nome.cognome@domain.tld
    (?P<email>
      [\w\d.+-]+       # nome utente
      @
      ([\w\d.]+\.)+    # prefisso del nome di dominio
      (com|org|edu)    # limita i domini di livello più alto consentiti
     )

    # Cerchiamo le parentesi angolari solo se l'asserzione look ahead le ha 
    # trovate entrambe
    (?(parentesi)>|\s*)

    $
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'Nome Cognome <nome.cognome@example.com>',
    u'Nessuna parentesi nome.cognome@example.com>',
    u'Parentesi aperta <nome.cognome@example.com',
    u'Parentesi chiusa nome.cognome@example.com>',
    u'no.parentesi@example.com',
    ]

for candidate in candidates:
    print
    print 'Candidato:', candidate
    match = address.search(candidate)
    if match:
        print '  Corrispondenza con name :', match.groupdict()['nome']
        print '  Corrispondenza con email:', match.groupdict()['email']
    else:
        print '  Nessuna Corrispondenza'