#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = 'Questa è una porzione di testo -- con punteggiatura.\nEd una seconda riga'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print 'Testo        :', repr(text)
print 'Modello      :', pattern
print 'Singola riga :', single_line.findall(text)
print 'Riga multipla:', multiline.findall(text)
