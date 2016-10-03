# re_fullmatch.py

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'
pattern = 'te'

print('Testo      :', text)
print('Modello    :', pattern)

m = re.search(pattern, text)
print('Search     :', m)
s = re.fullmatch(pattern, text)
print('Full match :', s)
