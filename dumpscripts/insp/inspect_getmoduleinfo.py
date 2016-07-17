#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import imp
import inspect
import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = 'example.py'

try:
    (name, suffix, mode, mtype)  = inspect.getmoduleinfo(filename)
except TypeError:
    print "Non si riesce a determinare il tipo di %s" % filename
else:
    mtype_name = { imp.PY_SOURCE:'sorgente',
                   imp.PY_COMPILED:'compilato',
                   }.get(mtype, mtype)

    mode_description = { 'rb':'(lettura-binario)',
                         'U':'(universal newline)',
                         }.get(mode, '')

    print 'NOME     :', name
    print 'SUFFISSO :', suffix
    print "MODALITA':", mode, mode_description
    print 'MTYPE    :', mtype_name