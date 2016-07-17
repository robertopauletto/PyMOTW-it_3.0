#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bz2

original_data = 'Questo è il testo originale.'

fmt = '%15s  %15s'
print fmt % ('len(data)', 'len(compressed)')
print fmt % ('-' * 15, '-' * 15)

for i in xrange(20):
    data = original_data * i
    compressed = bz2.compress(data)    
    print fmt % (len(data), len(compressed)), '*' if len(data) < len(compressed) else ''