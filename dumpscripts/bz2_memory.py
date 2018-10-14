# bz2_memory.py

import bz2
import binascii

original_data = b"Questo e' il testo originale."
print('Originale    : {} byte'.format(len(original_data)))
print(original_data)

print()
compressed = bz2.compress(original_data)
print('Compresso   : {} byte'.format(len(compressed)))
hex_version = binascii.hexlify(compressed)
for i in range(len(hex_version) // 40 + 1):
    print(hex_version[i * 40:(i + 1) * 40])

print()
decompressed = bz2.decompress(compressed)
print('Decompresso : {} byte'.format(len(decompressed)))
print(decompressed)
