# re_flags_dotall.py

import re

text = 'Test su di una porzione di testo -- con punteggiatura.\nUn\'altra riga.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print('Testo:\n  {!r}'.format(text))
print('Modello:\n  {}'.format(pattern))
print('No ritorni a capo :')
for match in no_newlines.findall(text):
    print('  {!r}'.format(match))
print('Dotall      :')
for match in dotall.findall(text):
    print('  {!r}'.format(match))
