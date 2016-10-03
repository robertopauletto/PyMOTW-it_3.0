# re_groups_named.py

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'

print(text)
print()

patterns = [
    r'^(?P<prima_parola>\w+)',
    r'(?P<ultima_parola>\w+)\S*$',
    r'(?P<parola_t>\bt\w+)\W+(?P<altra_parola>\w+)',
    r'(?P<finisce_con_o>\w+o)\b',
]

for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}'".format(pattern))
    print('  ', match.groups())
    print('  ', match.groupdict())
    print()

