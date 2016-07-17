#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import encodings

def search1(encoding):
    print 'ricerca1: Ricerca di :', encoding
    return None

def search2(encoding):
    print 'ricerca2: Ricerca di :', encoding
    return None

codecs.register(search1)
codecs.register(search2)

utf8 = codecs.lookup('utf-8')
print 'UTF-8:', utf8

try:
    unknown = codecs.lookup('questo-encoding-non-esiste')
except LookupError, err:
    print 'ERRORE:', err