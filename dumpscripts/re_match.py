#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'
pattern = 'te'

print 'Testo  :', text
print 'Modello:', pattern

m = re.match(pattern, text)
print 'Match  :', m
s = re.search(pattern, text)
print 'Search :', s
