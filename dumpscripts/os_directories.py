#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

dir_name = 'os_directories_example'

print 'Creazione', dir_name
os.makedirs(dir_name)

file_name = os.path.join(dir_name, 'esempio.txt')
print 'Creazione', file_name
f = open(file_name, 'wt')
try:
    f.write('file di esempio')
finally:
    f.close()

print 'Elenco', dir_name
print os.listdir(dir_name)

print 'Pulizia'
os.unlink(file_name)
os.rmdir(dir_name)
