# re_sub_named_groups.py

import re

bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')

text = 'Rendi questo  in **grassetto**. Anche **questo**.'

print('Testo:', text)
print('Grassetto:', bold.sub(r'<b>\g<bold_text></b>', text))

