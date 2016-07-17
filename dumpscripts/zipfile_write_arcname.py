#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from zipfile_infolist import print_info
import zipfile

zf = zipfile.ZipFile('zipfile_write_arcname.zip', mode='w')
try:
    zf.write('LEGGIMI.txt', arcname='NON_LEGGIMI.txt')
finally:
    zf.close()
print_info('zipfile_write_arcname.zip')
