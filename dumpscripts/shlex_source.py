# shlex_source.py

import shlex

text = "Questo testo dice di passare a source apici.txt prima di continuare."
print('ORIGINALE: {!r}'.format(text))
print()

lexer = shlex.shlex(text)
lexer.wordchars += '.'
lexer.source = 'source'

print('TOKEN:')
for token in lexer:
    print('{!r}'.format(token))
