#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import zipfile

zf = zipfile.ZipFile('esempio.zip')
for filename in [ 'LEGGIMI.txt', 'nonqui.txt' ]:
    try:
        data = zf.read(filename)
    except KeyError:
        print 'ERRORE: Non trovato %s nel file zip' % filename
    else:
        print filename, ':'
        print repr(data)
    print
