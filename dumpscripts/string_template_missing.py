# string_template_missing.py

import string


values = {'var': 'foo'}

t = string.Template("$var è qui ma $missing non è stato fornito")

try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERRORE:', str(err))

print('safe_substitute():', t.safe_substitute(values))
