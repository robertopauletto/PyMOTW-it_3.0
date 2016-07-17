#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import time

workers = []
for i in range(3):
    print 'GENITORE: Forking %s' % i
    worker_pid = os.fork()
    if not worker_pid:
        print 'WORKER %s: In partenza' % i
        time.sleep(2 + i)
        print 'WORKER %s: Sta finendo' % i
        sys.exit(i)
    workers.append(worker_pid)

for pid in workers:
    print 'GENITORE: In attesa di  %s' % pid
    done = os.waitpid(pid, 0)
    print 'GENITORE:', done
