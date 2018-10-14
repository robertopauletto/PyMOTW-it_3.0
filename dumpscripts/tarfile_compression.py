# tarfile_compression.py

import tarfile
import os

fmt = '{:<30} {:<10}'
print(fmt.format('NOME FILE', 'DIMENSIONE'))
print(fmt.format('LEGGIMI.txt', os.stat('LEGGIMI.txt').st_size))

FILES = [
    ('tarfile_compressione.tar', 'w'),
    ('tarfile_compressione.tar.gz', 'w:gz'),
    ('tarfile_compressione.tar.bz2', 'w:bz2'),
]

for filename, write_mode in FILES:
    with tarfile.open(filename, mode=write_mode) as out:
        out.add('LEGGIMI.txt')

    print(fmt.format(filename, os.stat(filename).st_size),
          end=' ')
    print([
        m.name
        for m in tarfile.open(filename, 'r:*').getmembers()
    ])
