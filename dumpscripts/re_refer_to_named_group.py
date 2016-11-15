# re_refer_to_named_group.py

import re

address = re.compile(
    '''

    # Il nome normale
    (?P<first_name>\w+)
    \s+
    (([\w.]+)\s+)?      # secondo nome opzionale od iniziali
    (?P<last_name>\w+)

    \s+

    <

    # Indirizzo: nome.cognome@domain.tld
    (?P<email>
      (?P=first_name)
      \.
      (?P=last_name)
      @
      ([\w\d.]+\.)+    # prefisso del nome di dominio
      (com|org|edu)    # limita i domini di livello più alto consentiti
    )

    >
    ''',
    re.VERBOSE | re.IGNORECASE)

candidates = [
    u'Nome Cognome <nome.cognome@example.com>',
    u'Diverso Nome <nome.cognome@example.com>',
    u'Nome SecondoNome Cognome <nome.cognome@example.com>',
    u'Nome S. Cognome <nome.cognome@example.com>',
    ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('  Corrispondenza con nome :', match.groupdict()['first_name'],
              end=' ')
        print(match.groupdict()['last_name'])
        print('  Corrispondenza con email:', match.groupdict()['email'])
    else:
        print('  Nessuna corrispondenza')

