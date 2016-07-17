#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re

patterns = [ 'questo', 'quello' ]
text = 'questo testo ha corrispondenza nel modello?'

for pattern in patterns:
    print 'Ricerca di "%s" in "%s" ->' % (pattern, text),

    if re.search(pattern,  text):
        print 'trovata corrispondenza!'
    else:
        print 'nessuna corrispondenza'