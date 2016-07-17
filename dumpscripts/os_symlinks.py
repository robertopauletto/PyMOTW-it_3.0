#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, tempfile

link_name = tempfile.mktemp()

print 'Creazione del link %s -> %s' % (link_name, __file__)
os.symlink(__file__, link_name)

stat_info = os.lstat(link_name)
print 'Permissi:', oct(stat_info.st_mode)

print 'Punta a:', os.readlink(link_name)

# Pulizia
os.unlink(link_name)
