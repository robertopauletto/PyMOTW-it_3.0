#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile
import time

t = tarfile.open('esempio.tar', 'r')
for member_info in t.getmembers():
    print member_info.name
    print '\tModificato:\t', time.ctime(member_info.mtime)
    print '\tModalità  :\t', oct(member_info.mode)
    print '\tTipo      :\t', member_info.type
    print '\tDimensione:\t', member_info.size, 'bytes'
    print
 