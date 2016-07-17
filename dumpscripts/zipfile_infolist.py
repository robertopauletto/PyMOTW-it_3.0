#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import zipfile

def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name)
    for info in zf.infolist():
        print info.filename
        print '\tCommento:\t', info.comment
        print '\tModificato:\t', datetime.datetime(*info.date_time)
        print '\tSistema:\t', info.create_system, '(0 = Windows, 3 = Unix)'
        print '\tversione ZIP:\t', info.create_version
        print '\tCompressi:\t', info.compress_size, 'byte'
        print '\tNon compressi:\t', info.file_size, 'byte'
        print

if __name__ == '__main__':
    print_info('esempio.zip')
