#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'questo',
                                     'quello',
                                     ]
            ]
text = 'questo testo ha corrispondenza nel modello?'

for regex in regexes:
    print 'Ricerca di "%s" in "%s" ->' % (regex.pattern, text),

    if regex.search(text):
        print 'trovata corrispondenza!'
    else:
        print 'nessuna corrispondenza'