# bz2_unicode.py

import bz2
import os

data = 'Carattere accentato å'

with bz2.open('esempio.bz2', 'wt', encoding='utf-8') as output:
    output.write(data)

with bz2.open('esempio.bz2', 'rt', encoding='utf-8') as input:
    print('File completo: {}'.format(input.read()))

# Spostamento all'inizio del carattere accentato.
with bz2.open('esempio.bz2', 'rt', encoding='utf-8') as input:
    input.seek(20)
    print('Un carattere: {}'.format(input.read(1)))

# Spostamento in mezzo al carattere accentato
with bz2.open('esempio.bz2', 'rt', encoding='utf-8') as input:
    input.seek(21)
    try:
        print(input.read(1))
    except UnicodeDecodeError:
        print('ERRORE: decodifica fallita')
