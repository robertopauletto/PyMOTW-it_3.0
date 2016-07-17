#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import zlib

lorem = open('lorem.txt', 'rt').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

print 'Decompressi che corrispondono a lorem       :', decompressed == lorem
print 'Dati inutilizzati che corrispondono a lorem :', decompressor.unused_data == lorem
