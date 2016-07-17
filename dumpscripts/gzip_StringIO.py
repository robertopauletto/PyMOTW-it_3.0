#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gzip
from cStringIO import StringIO
import binascii

uncompressed_data = 'La stessa riga, ripetutamente.\n' * 10
print 'NON COMPRESSI:', len(uncompressed_data)
print uncompressed_data

buf = StringIO()
f = gzip.GzipFile(mode='wb', fileobj=buf)
try:
    f.write(uncompressed_data)
finally:
    f.close()

compressed_data = buf.getvalue()
print 'COMPRESSI:', len(compressed_data)
print binascii.hexlify(compressed_data)

inbuffer = StringIO(compressed_data)
f = gzip.GzipFile(mode='rb', fileobj=inbuffer)
try:
    reread_data = f.read(len(uncompressed_data))
finally:
    f.close()

print
print 'RILETTURA:', len(reread_data)
print reread_data
