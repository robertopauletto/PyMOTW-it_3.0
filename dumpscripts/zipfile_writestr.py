#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from zipfile_infolist import print_info
import zipfile

msg = 'Questi dati non esistevano in un file prima di essere aggiunti al file ZIP'
zf = zipfile.ZipFile('zipfile_writestr.zip', 
                     mode='w',
                     compression=zipfile.ZIP_DEFLATED, 
                     )
try:
    zf.writestr('da_una_stringa.txt', msg)
finally:
    zf.close()

print_info('zipfile_writestr.zip')

zf = zipfile.ZipFile('zipfile_writestr.zip', 'r')
print zf.read('da_una_stringa.txt')
