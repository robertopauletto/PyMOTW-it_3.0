#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re

pattern = 'questo'
text = 'questo testo ha corrispondenza nel modello?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print 'Trovato "%s" in "%s" da %d a %d ("%s")' % \
    (match.re.pattern, match.string, s, e, text[s:e])