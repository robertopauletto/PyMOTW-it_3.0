#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gzip
import itertools
import os

output = gzip.open('righe_di_esempio.txt.gz', 'wb')
try:
    output.writelines(itertools.repeat('La stessa riga, ripetutamente.\n', 10))
finally:
    output.close()

os.system('gzcat righe_di_esempio.txt.gz')

