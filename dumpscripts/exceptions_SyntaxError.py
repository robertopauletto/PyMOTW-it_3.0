#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
    print eval('cinque volte tre')
except SyntaxError, err:
    print 'Errore di sintassi %s (%s-%s): %s' % \
        (err.filename, err.lineno, err.offset, err.text)
    print err
