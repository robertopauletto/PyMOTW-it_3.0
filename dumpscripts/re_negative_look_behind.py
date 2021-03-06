# re_negative_look_behind.py

import re

address = re.compile(
    '''
    ^

    # Un indirizzo: username@domain.tld

    [\w\d.+-]+       # nome utente

    # Ignora gli indirizzi noreply
    (?<!noreply)

    @
    ([\w\d.]+\.)+    # prefisso del nome di dominio
    (com|org|edu)    # limita i domini di livello più alto consentiti

    $
    ''',
    re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'noreply@example.com',
]

for candidate in candidates:
    print('Candidati:', candidate)
    match = address.search(candidate)
    if match:
        print('  Corrispondenza:', candidate[match.start():match.end()])
    else:
        print('  Nessuna corrispondenza')
