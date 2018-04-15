# shlex_example.py

import shlex
import sys

if len(sys.argv) != 2:
    print('Prego specificare un nome file da riga di comando.')
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r') as f:
    body = f.read()
print('ORIGINALE: {!r}'.format(body))
print()

print('TOKEN:')
lexer = shlex.shlex(body)
for token in lexer:
    print('{!r}'.format(token))
