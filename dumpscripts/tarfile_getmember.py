#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile
import time

t = tarfile.open('esempio.tar', 'r')
for filename in [ 'LEGGIMI.txt', 'nonqui.txt' ]:
    try:
        info = t.getmember(filename)
    except KeyError:
        print "ERRORE: Non trovato %s nell'archivio tar" % filename
    else:
        print '%s è di %d bytes' % (info.name, info.size)
