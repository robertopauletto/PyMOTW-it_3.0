#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import zipfile

zf = zipfile.ZipFile('esempio.zip')
for filename in [ 'LEGGIMI.txt', 'nonqui.txt' ]:
    try:
        info = zf.getinfo(filename)
    except KeyError:
        print 'ERRORE: Non trovato %s nel file zip' % filename
    else:
        print '%s è di %d byte' % (info.filename, info.file_size)
