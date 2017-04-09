# base64_base32.py

import base64

original_data = b'Questi sono i dati, in chiaro.'
print('Originale    :', original_data)

encoded_data = base64.b32encode(original_data)
print('Codificato   :', encoded_data)

decoded_data = base64.b32decode(encoded_data)
print('Decodificato :', decoded_data)
