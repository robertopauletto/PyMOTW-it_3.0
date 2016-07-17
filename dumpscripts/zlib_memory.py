#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import zlib
import binascii

original_data = 'Questo è il testo originale.'
print 'Originale    :', len(original_data), original_data

compressed = zlib.compress(original_data)
print 'Compresso    :', len(compressed), binascii.hexlify(compressed)

decompressed = zlib.decompress(compressed)
print 'Decompresso  :', len(decompressed), decompressed
