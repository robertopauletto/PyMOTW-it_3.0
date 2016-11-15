# re_subn.py

import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Rendi questo  in **grassetto**. Anche **questo**.'

print('Testo:', text)
print('Grassetto:', bold.subn(r'<b>\1</b>', text))
