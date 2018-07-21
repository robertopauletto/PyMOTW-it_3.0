# hmac_base64.py

import base64
import hmac
import hashlib

with open('lorem.txt', 'rb') as f:
    body = f.read()

hash = hmac.new(
    b'la-chiave-segreta-condivisa-va-qui',
    body,
    hashlib.sha1,
)

digest = hash.digest()
print(base64.encodestring(digest))
