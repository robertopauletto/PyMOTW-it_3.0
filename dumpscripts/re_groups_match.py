# re_groups_match.py

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'
print(text)
print()

patterns = [
    (r'^(\w+)', 'parola ad inizio stringa'),
    (r'(\w+)\S*$', 'parola alla fine, with punteggiatura opzionale'),
    (r'(\bt\w+)\W+(\w+)', 'parola che inizia con t, poi un\'altra parola'),
    (r'(\w+o)\b', 'parola che finisce con o'),
]

for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}' ({})\n".format(pattern, desc))
    print('  ', match.groups())
    print()
