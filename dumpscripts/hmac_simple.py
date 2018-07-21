# hmac_simple.py

import hmac

digest_maker = hmac.new(b'la-chiave-segreta-condivisa-va-qui')

with open('lorem.txt', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)
