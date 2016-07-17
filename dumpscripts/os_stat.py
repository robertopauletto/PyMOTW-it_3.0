#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import time

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

stat_info = os.stat(filename)

print 'os.stat(%s):' % filename
print '\tDimensione:', stat_info.st_size
print '\tPermissi:', oct(stat_info.st_mode)
print '\tProprietario:', stat_info.st_uid
print '\tDispositivo:', stat_info.st_dev
print '\tUltima modifica:', time.ctime(stat_info.st_mtime)
