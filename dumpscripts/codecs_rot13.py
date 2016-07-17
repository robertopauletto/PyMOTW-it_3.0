#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from cStringIO import StringIO

buffer = StringIO()
stream = codecs.getwriter('rot_13')(buffer)

text = 'abcdefghijklmnopqrstuvwxyz'

stream.write(text)
stream.flush()

print 'Originale:', text
print 'ROT-13   :', buffer.getvalue()