# re_look_ahead.py

import re

address = re.compile(
    '''
    # Un nome è composto da lettere, e può comprendere "." per abbreviazioni
    # ed iniziali del secondo nome
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+
     )
     \s+
    ) # il nome non è più opzionale

    # RICERCA IN AVANTI
    # Gli indirizzi email sono incorporati in parentesi angolari, solo se
    # sono presenti entrambe, oppure nessuna.
    (?= (<.*>$)       # il resto è racchiuso tra parentesi angolari
        |
        ([^<].*[^>]$) # il resto *non* è racchiuso tra parentesi angolari
      )

    <? # parentesi angolare di apertura opzionale

    # L'indirizzo stesso: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # nome utente
      @
      ([\w\d.]+\.)+    # prefisso del nome di dominio
      (com|org|edu)    # limita ai domini di livello più alto consentiti
    )

    >? # parentesi angolare di chiusura opzionale
    ''',
    re.VERBOSE)

candidates = [
    u'Nome Cognome <first.last@example.com>',
    u'Nessuna parentesi first.last@example.com',
    u'Parentesi di apertura <first.last@example.com',
    u'Parentesi di chiusura first.last@example.com>',
]

for candidate in candidates:
    print('Candidato:', candidate)
    match = address.search(candidate)
    if match:
        print('  Nome :', match.groupdict()['name'])
        print('  Email:', match.groupdict()['email'])
    else:
        print('  Nessuna corrispondenza')
