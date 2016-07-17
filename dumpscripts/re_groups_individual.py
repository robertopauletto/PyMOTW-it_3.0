#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = 'Questa è una porzione di testo -- con punteggiatura.'

print 'Testo in input              :', text

# parola che inizia con 't, poi un'altra parola
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print 'Modello di corrispondenza   :', regex.pattern

match = regex.search(text)
print 'Intera corrispondenza       :', match.group(0)
print 'Parola inizia con  "t"      :', match.group(1)
print 'Parola dopo la parola con"t":', match.group(2)