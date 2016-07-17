#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import getpass
import sys

if sys.stdin.isatty():
    p = getpass.getpass('Si usa getpass: ')
else:
    print 'Si usa readline'
    p = sys.stdin.readline().rstrip()

print 'Letto: ', p