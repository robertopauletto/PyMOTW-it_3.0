#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, sys

# Se non viene passato un percorso da elencare, si usa /tmp
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print '\n', dir_name
    # Aggiunge ai nomi delle sotto direcotry una /
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Combina i contenuti delle directory assieme
    contents = sub_dirs + files
    contents.sort()
    # Mostra il contenuto
    for c in contents:
        print '\t%s' % c
