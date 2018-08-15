# zlib_mixed.py

import zlib

lorem = open('lorem.txt', 'rb').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print('I dati decompressi corrispondono al lorem:', decompressed_matches)

unused_matches = decompressor.unused_data == lorem
print('Dati non utilizzati corrispondono al lorem :', unused_matches)
