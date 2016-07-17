#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

import urllib
import os

def reporthook(blocks_read, block_size, total_size):
    if not blocks_read:
        print 'Connessione aperta'
        return
    if total_size < 0:
        # Dimensione sconosciuta
        print 'Letti %d blocchi' % blocks_read
    else:
        amount_read = blocks_read * block_size
        print 'Letti %d blocchi, oppure %d/%d' % (blocks_read, amount_read, total_size)
    return

try:
    filename, msg = urllib.urlretrieve('http://blog.doughellmann.com/', reporthook=reporthook)
    print
    print 'File:', filename
    print 'Headers:'
    print msg
    print 'Il file esiste prima della pulizia:', os.path.exists(filename)

finally:
    urllib.urlcleanup()

    print 'Il file esiste ancora:', os.path.exists(filename)