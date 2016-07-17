#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import re

text = 'Paragrafo uno\nsu due righe.\n\nParagrafo due.\n\n\nParagrafo tre.'
   
print 'Con findall:'
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)', text, flags=re.DOTALL)):
    print num, repr(para)
    print

print
print 'Con split:'
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print num, repr(para)
    print
    