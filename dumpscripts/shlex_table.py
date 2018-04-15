# shlex_table.py

import shlex

text = """|Col 1||Col 2||Col 3|"""
print('ORIGINALE: {!r}'.format(text))
print()

lexer = shlex.shlex(text)
lexer.quotes = '|'

print('TOKEN:')
for token in lexer:
    print('{!r}'.format(token))
