# re_email_with_name.py

import re

address = re.compile(
    '''

    # Un nome è composto da lettere e può includere "." per titoli,
    # abbreviazini ed iniziali intermedie
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+)
       \s*
       # Gli indirizzi email sono racchiusi tra parentesi angolari: < >
       # solo se troviamo un nome, quindi
       # manteniamo la parentesi di partenza in questo gruppo
       <
    )? # # l'intero nome è opzionalre

    # L'indirizzo email vero e proprio: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # nome utente
      @
      ([\w\d.]+\.)+    # prefisso del nome di dominio
      (com|org|edu)    # limita i domini di livello più alto consentiti
    )

    >? # parentesi angolare di chiusura opzionale
    ''',
    re.VERBOSE)

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
    print('Candidato:', candidate)
    match = address.search(candidate)
    if match:
        print('  Nome :', match.groupdict()['name'])
        print('  Email:', match.groupdict()['email'])
    else:
        print('  Nessuna corrispondenza')

