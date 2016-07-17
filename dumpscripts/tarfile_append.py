#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile

print 'creazione archivio'
out = tarfile.open('tarfile_accoda.tar', mode='w')
try:
    out.add('LEGGIMI.txt')
finally:
    out.close()

print 'contenuto:', [m.name 
                    for m in tarfile.open('tarfile_accoda.tar', 'r').getmembers()]

print 'accodo index.rst'
out = tarfile.open('tarfile_accoda.tar', mode='a')
try:
    out.add('index.rst')
finally:
    out.close()

print 'contenuto:', [m.name 
                    for m in tarfile.open('tarfile_accoda.tar', 'r').getmembers()]
