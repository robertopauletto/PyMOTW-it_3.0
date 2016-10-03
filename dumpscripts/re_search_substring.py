# re_search_substring.py

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'
pattern = re.compile(r'\b\w*te\w*\b')

print('Testo:', text)
print()

pos = 0
while True:
    match = pattern.search(text, pos)
    if not match:
        break
    s = match.start()
    e = match.end()
    print('  {:>2d} : {:>2d} = "{}"'.format(
        s, e - 1, text[s:e]))
    # Si sposta in avanti nel testo per la ricerca successiva
    pos = e
