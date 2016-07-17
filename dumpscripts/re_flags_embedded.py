#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = 'Questo e quello.'
pattern = r'(?i)\bQ\w+'
regex = re.compile(pattern)

print 'Testo         :', text
print 'Modello       :', pattern
print 'Corrispondenza:', regex.findall(text)        