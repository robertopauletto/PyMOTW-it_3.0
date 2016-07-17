import gzip
import os
import hashlib

def get_hash(data):
    return hashlib.md5(data).hexdigest()

data = open('lorem.txt', 'r').read() * 1024
cksum = get_hash(data)

print 'Livello  Dimensione  Checksum'
print '-------  ----------  ---------------------------------'
print 'dati     %10d  %s' % (len(data), cksum)

for i in xrange(1, 10):
    filename = 'livello-di-compressione-%s.gz' % i
    output = gzip.open(filename, 'wb', compresslevel=i)
    try:
        output.write(data)
    finally:
        output.close()
    size = os.stat(filename).st_size
    cksum = get_hash(open(filename, 'rb').read())
    print '%5d    %10d  %s' % (i, size, cksum)
