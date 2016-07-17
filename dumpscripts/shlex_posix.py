#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shlex

for s in [ 'Da"Non"Separare',
           '"Da"Separare',
           'Escape \e Carattere non tra virgolette',
           'Escape "\e" Carattere tra virgolette',
           "Escape '\e' Carattere tra apici singoli",
           r"Escape '\'' \"\'\" singolo apice",
           r'Escape "\"" \'\"\' virgolette',
           "\"'Elimina uno strato extra di virgolette'\"",
           ]:
    print 'ORIGINALE :', repr(s)
    print 'non-POSIX:',

    non_posix_lexer = shlex.shlex(s, posix=False)
    try:
        print repr(list(non_posix_lexer))
    except ValueError, err:
        print 'errore(%s)' % err

    
    print 'POSIX    :',
    posix_lexer = shlex.shlex(s, posix=True)
    try:
        print repr(list(posix_lexer))
    except ValueError, err:
        print 'errore(%s)' % err

    print