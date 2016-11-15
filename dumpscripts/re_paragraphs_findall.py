# re_paragraphs_findall.py

import re

text = '''Paragrafo uno
su due righe.

Paragrafo due.


Paragrafo tre.'''

for num, para in enumerate(re.findall(r'(.+?)\n{2,}',
                                      text,
                                      flags=re.DOTALL)
                           ):
    print(num, repr(para))
    print()
