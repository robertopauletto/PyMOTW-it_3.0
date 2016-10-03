# re_simple_match.py

import re

pattern = 'questo'
text = 'questo testo ha corrispondenza nel modello?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Trovato "{}"\nin "{}"\nda {} a {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))
