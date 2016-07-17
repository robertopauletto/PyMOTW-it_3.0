#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import zipfile

for filename in [ 'LEGGIMI.txt', 'esempio.zip', 
                  'cattivo_esempio.zip', 'nonqui.zip' ]:
    print '%20s  %s' % (filename, zipfile.is_zipfile(filename))
