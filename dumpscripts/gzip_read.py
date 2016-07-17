#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gzip

input_file = gzip.open('esempio.txt.gz', 'rb')
try:
    print input_file.read()
finally:
    input_file.close()

