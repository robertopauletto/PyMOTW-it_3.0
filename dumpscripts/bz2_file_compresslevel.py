#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bz2
import os

data = open('lorem.txt', 'r').read() * 1024
print 'Input contiene %d byte' % len(data)

for i in xrange(1, 10):
    filename = 'livello-di-compressione-%s.bz2' % i
    output = bz2.BZ2File(filename, 'wb', compresslevel=i)
    try:
        output.write(data)
    finally:
        output.close()
    os.system('cksum %s' % filename)
