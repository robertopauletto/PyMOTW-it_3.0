#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shlex

text = """Questa riga va bene.
Questa riga ha un "virgolettato non completato.
Anche questa va bene.
"""

print 'ORIGINALE:', repr(text)
print

lexer = shlex.shlex(text)

print 'TOKEN:'
try:
    for token in lexer:
        print repr(token)
except ValueError, err:
    first_line_of_error = lexer.token.splitlines()[0]
    print 'ERRORE:', lexer.error_leader(), str(err), 'dopo "' + first_line_of_error + '"'