# re_split.py

import re

text = '''Paragrafo uno
su due righe.

Paragrafo due.


Paragrafo tre.'''

print('Con findall:')
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)',
                                      text,
                                      flags=re.DOTALL)):
    print(num, repr(para))
    print()

print()
print('Con split:')
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print(num, repr(para))
    print()

