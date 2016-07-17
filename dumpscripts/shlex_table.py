#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shlex

text = """|Col 1||Col 2||Col 3|"""
print 'ORIGINALE:', repr(text)
print

lexer = shlex.shlex(text)
lexer.quotes = '|'

print 'TOKEN:'
for token in lexer:
    print repr(token)