# mmap_read.py

import mmap

with open('lorem.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_READ) as m:
        print('Primi 10 byte tramite read :', m.read(10))
        print('Primi 10 byte tramite slice:', m[:10])
        print('Secondi 10 byte tramite read :', m.read(10))
