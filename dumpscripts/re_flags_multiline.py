# re_flags_multiline.py

import re

text = 'Test su di una porzione di testo -- con punteggiatura.\nUn\'altra riga.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print('Testo:\n  {!r}'.format(text))
print('Modello:\n  {}'.format(pattern))
print('Riga Singola :')
for match in single_line.findall(text):
    print('  {!r}'.format(match))
print('Multiriga    :')
for match in multiline.findall(text):
    print('  {!r}'.format(match))
