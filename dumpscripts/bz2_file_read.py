#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bz2

input_file = bz2.BZ2File('esempio.txt.bz2', 'rb')
try:
    print input_file.read()
finally:
    input_file.close()
