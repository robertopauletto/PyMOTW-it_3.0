#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import zipfile
from zipfile_infolist import print_info

msg = 'Questi dati non esistevano in un file prima di essere aggiunti al file ZIP'
zf = zipfile.ZipFile('zipfile_writestr_zipinfo.zip', 
                     mode='w',
                     )
try:
    info = zipfile.ZipInfo('da_una_stringa.txt', 
                           date_time=time.localtime(time.time()),
                           )
    info.compress_type=zipfile.ZIP_DEFLATED
    info.comment='I commenti vanno qui'
    info.create_system=0
    zf.writestr(info, msg)
finally:
    zf.close()

print_info('zipfile_writestr_zipinfo.zip')
