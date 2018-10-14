# bz2_mixed.py

import bz2

lorem = open('lorem.txt', 'rt').read().encode('utf-8')
compressed = bz2.compress(lorem)
combined = compressed + lorem

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print('Decompressi che corrispondono a lorem       :', decompressed_matches)

unused_matches = decompressor.unused_data == lorem
print('Dati inutilizzati che corrispondono a lorem :', unused_matches)
