# shlex_posix.py

import shlex

examples = [
    'Da"Non"Separare',
    '"Da"Separare',
    'Ignorare il Carattere \e se non tra apici',
    'Ignorare il Carattere "\e" se tra doppi apici',
    "Ignorare il Carattere '\e' se tra singoli apici",
    r"Ignorare '\'' \"\'\" tra singoli apici",
    r'Ignorare "\"" \'\"\' tra doppi apici',
    "\"'Togliere uno strato di apici supplementare'\"",
]

for s in examples:
    print('ORIGINALE : {!r}'.format(s))
    print('non-POSIX : ', end='')

    non_posix_lexer = shlex.shlex(s, posix=False)
    try:
        print('{!r}'.format(list(non_posix_lexer)))
    except ValueError as err:
        print('errore({})'.format(err))

    print('POSIX     : ', end='')
    posix_lexer = shlex.shlex(s, posix=True)
    try:
        print('{!r}'.format(list(posix_lexer)))
    except ValueError as err:
        print('error({})'.format(err))

    print()
