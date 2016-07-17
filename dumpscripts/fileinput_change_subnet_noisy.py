#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import fileinput
import glob
import sys

from_base = sys.argv[1]
to_base = sys.argv[2]
files = sys.argv[3:]

for line in fileinput.input(files, inplace=True):
    if fileinput.isfirstline():
        sys.stderr.write('Iniziata elaborazione %s\n' % fileinput.filename())
        sys.stderr.write('Contenuto della directory: %s\n' % glob.glob('etc_hosts.txt*'))
    line = line.rstrip().replace(from_base, to_base)
    print line

sys.stderr.write('Finita elaborazione\n')
sys.stderr.write('Contenuto della directory: %s\n' % glob.glob('etc_hosts.txt*'))
