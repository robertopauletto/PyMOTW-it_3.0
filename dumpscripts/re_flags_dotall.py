#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = u'Questa è una porzione di testo -- senza punteggiatura.\nEd una seconda riga'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print 'Testo             :', repr(text)
print 'Modello           :', pattern
print 'No ritorni a capo :', no_newlines.findall(text)
print 'Dotall            :', dotall.findall(text)