#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import re

text = 'Paragrafo uno\nsu due righe.\n\nParagrafo due.\n\n\nParagrafo tre.'

for num, para in enumerate(re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL)):
    print num, repr(para)
    print