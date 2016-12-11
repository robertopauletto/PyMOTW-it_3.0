# time_clock.py

import hashlib
import time

# Dati da usare per calcolare comme di controllo md5
data = open(__file__, 'rb').read()

for i in range(5):
    h = hashlib.sha1()
    print(time.ctime(), ': {:0.3f} {:0.3f}'.format(time.time(), time.clock()))
    for i in range(100000):
        h.update(data)
    cksum = h.digest()
