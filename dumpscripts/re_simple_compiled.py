# re_simple_compiled.py

import re

# Precompile the patterns
regexes = [
    re.compile(p)
    for p in ['questo', 'quello']
]
text = 'questo testo ha corrispondenza nel modello?'

print('Testo: {!r}\n'.format(text))

for regex in regexes:
    print('Ricerca di "{}" ->'.format(regex.pattern), end=' ')

    if regex.search(text):
        print('trovato!')
    else:
        print('non trovato')
