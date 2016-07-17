#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bz2
import os

output = bz2.BZ2File('esempio.txt.bz2', 'wb')
try:
    output.write('Il contenuto del file di esempio va qui..\n')
finally:
    output.close()

os.system('file esempio.txt.bz2')
