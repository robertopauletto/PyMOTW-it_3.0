#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile

t = tarfile.open('esempio.tar', 'r')
for filename in [ 'LEGGIMI.txt', 'nonqui.txt' ]:
    try:
        f = t.extractfile(filename)
    except KeyError:
        print "ERRORE: Non trovato %s nell'archivio tar" % filename
    else:
        print filename, ':', f.read()
