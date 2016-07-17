#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bz2
import binascii

original_data = 'Questo è il testo originale.'
print 'Originale    :', len(original_data), original_data

compressed = bz2.compress(original_data)
print 'Compresso    :', len(compressed), binascii.hexlify(compressed)

decompressed = bz2.decompress(compressed)
print 'Decompresso  :', len(decompressed), decompressed
