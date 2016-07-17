#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from zipfile_infolist import print_info
import zipfile

print 'creazione archivio'
zf = zipfile.ZipFile('zipfile_append.zip', mode='w')
try:
    zf.write('LEGGIMI.txt')
finally:
    zf.close()

print
print_info('zipfile_append.zip')

print "accoda all'archivio"
zf = zipfile.ZipFile('zipfile_append.zip', mode='a')
try:
    zf.write('LEGGIMI.txt', arcname='LEGGIMI2.txt')
finally:
    zf.close()

print
print_info('zipfile_append.zip')
