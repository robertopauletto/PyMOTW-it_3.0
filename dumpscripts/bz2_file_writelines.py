#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bz2
import itertools
import os

output = bz2.BZ2File('righe_di_esempio.txt.bz2', 'wb')
try:
    output.writelines(itertools.repeat('La stessa riga, ripetutamente.\n', 10))
finally:
    output.close()

    os.system('bzcat righe_di_esempio.txt.bz2')
