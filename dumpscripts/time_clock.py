#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
import time

# Dati da usare per calcolare i checksums md5
data = open(__file__, 'rt').read()

for i in range(5):
    h = hashlib.sha1()
    print time.ctime(), ': %0.3f %0.3f' % (time.time(), time.clock())
    for i in range(100000):
        h.update(data)
    cksum = h.digest()
