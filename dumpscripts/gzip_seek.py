#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gzip

input_file = gzip.open('esempio.txt.gz', 'rb')
try:
    print 'Intero file:'
    all_data = input_file.read()
    print all_data
    
    expected = all_data[5:15]
    
    # porta il puntatore ad inizio file
    input_file.seek(0)
    
    # si sposta di 5 byte
    input_file.seek(5)
    print 'A partire da posizione 5 per 10 byte:'
    partial = input_file.read(10)
    print partial
    
    print
    print expected == partial
finally:
    input_file.close()
