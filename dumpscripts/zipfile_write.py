#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from zipfile_infolist import print_info
import zipfile

print 'creazione archivio'
zf = zipfile.ZipFile('zipfile_write.zip', mode='w')
try:
    print 'aggiungo LEGGIMI.txt'
    zf.write('LEGGIMI.txt')
finally:
    print 'chiusura'
    zf.close()

print
print_info('zipfile_write.zip')
