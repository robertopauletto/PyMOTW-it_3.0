# base64_base16.py

import base64

original_data = b'Questi sono i dati, in chiaro.'
print('Originali    :', original_data)

encoded_data = base64.b16encode(original_data)
print('Codificati   :', encoded_data)

decoded_data = base64.b16decode(encoded_data)
print('Decodificati :', decoded_data)
