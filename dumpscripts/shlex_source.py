#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shlex

text = """Questo testo dice di includere source quotes.txt prima di continuare."""
print 'ORIGINALE:', repr(text)
print

lexer = shlex.shlex(text)
lexer.wordchars += '.'
lexer.source = 'source'

print 'TOKEN:'
for token in lexer:
    print repr(token)