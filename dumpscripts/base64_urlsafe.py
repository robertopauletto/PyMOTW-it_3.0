# base64_urlsafe.py

import base64

encodes_with_pluses = b'\xfb\xef'
encodes_with_slashes = b'\xff\xff'

for original in [encodes_with_pluses, encodes_with_slashes]:
    print('Originale              :', repr(original))
    print('Codifica standard      :',
          base64.standard_b64encode(original))
    print('Codifica a prova di URL:',
          base64.urlsafe_b64encode(original))
    print()
