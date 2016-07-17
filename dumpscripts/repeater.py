#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys

sys.stderr.write('repeater.py: inizio\n')
sys.stderr.flush()

while True:
    next_line = sys.stdin.readline()
    if not next_line:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

sys.stderr.write('repeater.py: uscita\n')
sys.stderr.flush()
