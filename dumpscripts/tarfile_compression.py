#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile
import os

fmt = '%-30s %-10s'
print fmt % ('NOME FILE', 'DIMENSIONE')
print fmt % ('LEGGIMI.txt', os.stat('LEGGIMI.txt').st_size)

for filename, write_mode in [
    ('tarfile_compressione.tar', 'w'),
    ('tarfile_compressione.tar.gz', 'w:gz'),
    ('tarfile_compressione.tar.bz2', 'w:bz2'),
    ]:
    out = tarfile.open(filename, mode=write_mode)
    try:
        out.add('LEGGIMI.txt')
    finally:
        out.close()

    print fmt % (filename, os.stat(filename).st_size),
    print [m.name for m in tarfile.open(filename, 'r:*').getmembers()]
