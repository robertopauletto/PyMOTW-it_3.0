#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import time

for i in range(3):
    print 'GENITORE: Forking %s' % i
    worker_pid = os.fork()
    if not worker_pid:
        print 'WORKER %s: In partenza' % i
        time.sleep(2 + i)
        print 'WORKER %s: Sta finendo' % i
        sys.exit(i)

for i in range(3):
    print 'GENITORE: In attesa di %s' % i
    done = os.wait()
    print 'GENITORE:', done
