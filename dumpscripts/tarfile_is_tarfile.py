#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile

for filename in [ 'LEGGIMI.txt', 'esempio.tar', 
                  'cattivo_esempio.tar', 'nonqui.tar' ]:
    try:
        print '%20s  %s' % (filename, tarfile.is_tarfile(filename))
    except IOError, err:
        print '%20s  %s' % (filename, err)
