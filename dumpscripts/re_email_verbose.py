# re_email_verbose.py

import re

address = re.compile(
    '''
    [\w\d.+-]+       # nome utente
    @
    ([\w\d.]+\.)+    # prefisso del nome di dominio
    (com|org|edu)    # TODO: supportare altri livelli principali di dominio
    ''',
    re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
]

for candidate in candidates:
    match = address.search(candidate)
    print('{:<30}  {}'.format(
        candidate, 'Corrispondenza' if match else 'Nessuna Corrispondenza'),
    )

