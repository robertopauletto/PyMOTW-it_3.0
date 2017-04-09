# base64_b64decode.py

import base64

encoded_data = b'UXVlc3RpIHNvbm8gaSBkYXRpLCBpbiBjaGlhcm8='
decoded_data = base64.b64decode(encoded_data)
print('Codificati   :', encoded_data)
print('Decodificati :', decoded_data)
