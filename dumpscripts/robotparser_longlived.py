#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import robotparser
import time
import urlparse

AGENT_NAME = 'PyMOTW'
parser = robotparser.RobotFileParser()
# Si usa la copia locale
parser.set_url('robots.txt')
parser.read()
parser.modified()

PATHS = [
    '/',
    '/PyMOTW/',
    '/admin/',
    '/downloads/PyMOTW-1.92.tar.gz',
    ]

for n, path in enumerate(PATHS):
    print
    age = int(time.time() - parser.mtime())
    print 'age:', age,
    if age > 1:
        print 'rilettura di robots.txt'
        parser.read()
        parser.modified()
    else:
        print
    print '%6s : %s' % (parser.can_fetch(AGENT_NAME, path), path)
    # Simulazione di un ritardo nell'elaborazione
    time.sleep(1)
