#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import dircache
import os

path = '/tmp'
file_to_create = os.path.join(path, 'pymotw_tmp.txt')

# Ottiene il contenuto della directory
first = dircache.listdir(path)

# Crea un nuovo file
open(file_to_create, 'wt').close()

# Rielabora il contenuto della directory
second = dircache.listdir(path)

# Elimina il file appena creato
os.unlink(file_to_create)

print 'Identica  :', first is second
print 'Uguale    :', first == second
print 'Differenze:', list(set(second) - set(first))
