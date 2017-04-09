# base64_base85.py

import base64

original_data = b'TQuesti sono i dati, in chiaro.'
print('Originale    : {} byte {!r}'.format(
    len(original_data), original_data))

b64_data = base64.b64encode(original_data)
print('Codifica b64 : {} byte {!r}'.format(
    len(b64_data), b64_data))

b85_data = base64.b85encode(original_data)
print('Codifica b85 : {} byte {!r}'.format(
    len(b85_data), b85_data))

a85_data = base64.a85encode(original_data)
print('Codifica a85 : {} byte {!r}'.format(
    len(a85_data), a85_data))
