#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile

print 'creazione archivio'
out = tarfile.open('tarfile_aggiunto.tar', mode='w')
try:
    print 'aggiunta di LEGGIMI.txt'
    out.add('LEGGIMI.txt')
finally:
    print 'chiusura'
    out.close()

print
print 'Contenuto:'
t = tarfile.open('tarfile_aggiunto.tar', 'r')
for member_info in t.getmembers():
    print member_info.name

