#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

twitter = re.compile(
    '''
    # Un twitter handle: @username
    (?<=@)
    ([\w\d_]+)       # nome utente
    ''',
    re.UNICODE | re.VERBOSE)

text = '''Questo testo include due Twitter handle.
Uno per @ThePSF, ed uno per l'autore, @doughellmann.
'''

print text
for match in twitter.findall(text):
    print 'Handle:', match