#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile
from cStringIO import StringIO

data = "Questi sono i dati da scrivere nell'archivio."

out = tarfile.open('tarfile_aggiungifile_stringa.tar', mode='w')
try:
    info = tarfile.TarInfo('made_up_file.txt')
    info.size = len(data)
    out.addfile(info, StringIO(data))
finally:
    out.close()

print
print 'Contenuto:'
t = tarfile.open('tarfile_aggiungifile_stringa.tar', 'r')
for member_info in t.getmembers():
    print member_info.name
    f = t.extractfile(member_info)
    print f.read()
