#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import zlib

original_data = 'Questo è il testo originale.'

fmt = '%15s  %15s'
print fmt % ('len(dati)', 'len(compressi)')
print fmt % ('-' * 15, '-' * 15)

for i in xrange(20):
    data = original_data * i
    compressed = zlib.compress(data)    
    print fmt % (len(data), len(compressed)), '*' if len(data) < len(compressed) else ''
