# mmap_write_copy.py
import mmap
import shutil

# Copy the example file
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'
reversed = word[::-1]

with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_COPY) as m:
        print('Prima in memoria:\n{}'.format(
            m.readline().rstrip()))
        print('Dopo nel file   :\n{}\n'.format(
            f.readline().rstrip()))

        m.seek(0)  # torna ad inizio file
        loc = m.find(word)
        m[loc:loc + len(word)] = reversed

        m.seek(0)  # torna ad inizio file
        print('Prima in memoria :\n{}'.format(
            m.readline().rstrip()))

        f.seek(0)
        print('Dopo nel file    :\n{}'.format(
            f.readline().rstrip()))
