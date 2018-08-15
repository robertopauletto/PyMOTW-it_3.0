# zlib_incremental.py

import zlib
import binascii

compressor = zlib.compressobj(1)

with open('lorem.txt', 'rb') as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('Compressi: {}'.format(
                binascii.hexlify(compressed)))
        else:
            print('nel buffer...')
    remaining = compressor.flush()
    print('Svuotamento: {}'.format(binascii.hexlify(remaining)))
