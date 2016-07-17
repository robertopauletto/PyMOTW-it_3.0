#!/usr/bin/env python
# -*- coding: Latin-1 -*-

import linecache
from linecache_data import *

filename = make_tempfile()

# Estrazione della stessa riga dalla sorgente e dalla cache.
# (Notare che linecache conta da 1)
print 'SORGENTE: ', lorem.split('\n')[4]
print 'CACHE   : ', linecache.getline(filename, 5).rstrip()

cleanup(filename)
