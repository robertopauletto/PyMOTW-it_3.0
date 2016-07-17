#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print 'Trovato "%s"' % match