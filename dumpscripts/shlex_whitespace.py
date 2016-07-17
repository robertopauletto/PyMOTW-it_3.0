#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shlex
import sys

if len(sys.argv) != 2:
    print 'Per favore specificare un nome di file nella riga di comando.'
    sys.exit(1)

filename = sys.argv[1]
body = file(filename, 'rt').read()
print 'ORIGINALE:', repr(body)
print

print 'TOKEN:'
lexer = shlex.shlex(body)
lexer.whitespace += '.,'
for token in lexer:
    print repr(token)