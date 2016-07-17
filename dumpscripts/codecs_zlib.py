#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from cStringIO import StringIO

from codecs_to_hex import to_hex

buffer = StringIO()
stream = codecs.getwriter('zlib')(buffer)

text = 'abcdefghijklmnopqrstuvwxyz\n' * 50

stream.write(text)
stream.flush()

print 'Lunghezza originale      :', len(text)
compressed_data = buffer.getvalue()
print 'Compressione ZIP         :', len(compressed_data)

buffer = StringIO(compressed_data)
stream = codecs.getreader('zlib')(buffer)

first_line = stream.readline()
print 'Lettura della prima riga :', repr(first_line)

uncompressed_data = first_line + stream.read()
print 'Non compresso            :', len(uncompressed_data)
print 'Uguale                   :', text == uncompressed_data