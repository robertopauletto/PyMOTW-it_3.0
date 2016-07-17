#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import itertools

# Tentativo di creare un MemoryError allocando molta memoria
l = []
for i in range(3):
    try:
        for j in itertools.count(1):
            print i, j
            l.append('*' * (2**30))
    except MemoryError:
        print '(errore, si svuota la lista esistente)'
        l = []
