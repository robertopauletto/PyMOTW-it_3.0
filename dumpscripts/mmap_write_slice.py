# mmap_write_slice.py

import mmap
import shutil

# Copia il file di esempio
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'
reversed = word[::-1]
print('Ricerca di        :', word)
print('Da sostituire con :', reversed)

with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print('Prima:\n{}'.format(m.readline().rstrip()))
        m.seek(0)  # torna ad inizio file

        loc = m.find(word)
        m[loc:loc + len(word)] = reversed
        m.flush()

        m.seek(0)  # torna ad inizio file
        print('Dopo  :\n{}'.format(m.readline().rstrip()))

        f.seek(0)  # torna ad inizio file
        print('File  :\n{}'.format(f.readline().rstrip()))
