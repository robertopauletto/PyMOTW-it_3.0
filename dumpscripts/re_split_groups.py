# re_split_groups.py

import re

text = '''Paragrafo uno
su due righe.

Paragrafo due.


Paragrafo tre.'''

print('Con split:')
for num, para in enumerate(re.split(r'(\n{2,})', text)):
    print(num, repr(para))
    print()
