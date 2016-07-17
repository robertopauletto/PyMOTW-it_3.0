#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile

print 'creazione archivio'
out = tarfile.open('tarfile_aggiungifile.tar', mode='w')
try:
    print 'aggiunto LEGGIMI.txt come RINOMINATO.txt'
    info = out.gettarinfo('LEGGIMI.txt', arcname='RINOMINATO.txt')
    out.addfile(info)
finally:
    print 'chiusura'
    out.close()

print
print 'Contenuto:'
t = tarfile.open('tarfile_aggiungifile.tar', 'r')
for member_info in t.getmembers():
    print member_info.name

