# re_refer_to_group.py

import re

address = re.compile(
    r'''

    # Il nome normale
    (\w+)               # nome
    \s+
    (([\w.]+)\s+)?      # Secondo nome opzionale od iniziale
    (\w+)               # cognome

    \s+

    <

    # Indirizzo: nome.cognome@domain.tld
    (?P<email>
      \1               # nome
      \.
      \4               # cognome
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
    print('Candidato:', candidate)
    match = address.search(candidate)
    if match:
        print('  Corrispondenza con nome :', match.group(1), match.group(4))
        print('  Corrispondenza con email:', match.group(5))
    else:
        print('  Nessuna corrispondenza')
