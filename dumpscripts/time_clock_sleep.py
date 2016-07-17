#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time

for i in range(6, 1, -1):
    print '%s %0.2f %0.2f' % (time.ctime(), time.time(), time.clock())
    print 'In pausa', i
    time.sleep(i)
