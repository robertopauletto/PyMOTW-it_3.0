# base64_b64encode.py
# -*- coding: utf-8 -*-
#end_pymotw_header

import base64
import textwrap

# Carica questo file sorgente ed elimina l'intestazione
with open(__file__, 'r', encoding='utf-8') as input:
    raw = input.read()
    initial_data = raw.split('#end_pymotw_header')[1]

byte_string = initial_data.encode('utf-8')
encoded_data = base64.b64encode(byte_string)
wrapped_data = textwrap.fill(str(encoded_data), width=50)

num_initial = len(byte_string)

padding = 3 - (num_initial % 3)

print('{} byte prima della codifica'.format(num_initial))
print('Attesi {} byte di riempimento'.format(padding))
print('{} byte dopo la codifica\n'.format(len(encoded_data)))
print(wrapped_data)
