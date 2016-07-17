#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from zipfile_infolist import print_info
import zipfile
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = { zipfile.ZIP_DEFLATED: 'compresso',
          zipfile.ZIP_STORED:   'archiviato senza compressione',
          }

print 'creazione archivio'
zf = zipfile.ZipFile('zipfile_write_compression.zip', mode='w')
try:
    print 'aggiunta di LEGGIMI.txt con modalità di compressione', modes[compression]
    zf.write('LEGGIMI.txt', compress_type=compression)
finally:
    print 'chiusura'
    zf.close()

print
print_info('zipfile_write_compression.zip')
