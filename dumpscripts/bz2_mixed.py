#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bz2

lorem = open('lorem.txt', 'rt').read()
compressed = bz2.compress(lorem)
combined = compressed + lorem

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(combined)

print 'Decompressi che corrispondono a lorem       :', decompressed == lorem
print 'Dati inutilizzati che corrispondono a lorem :', decompressor.unused_data == lorem
