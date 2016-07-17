#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

text = 'Questo e quello'
pattern = r'\bQ\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

print 'Testo           :', text
print 'Modello         :', pattern
print 'Case-sensitive  :', with_case.findall(text)
print 'Case-insensitive:', without_case.findall(text)