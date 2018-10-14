# bz2_file_compresslevel.py

import bz2
import io
import os

data = open('lorem.txt', 'r', encoding='utf-8').read() * 1024
print('Input coniene  {} byte'.format(
    len(data.encode('utf-8'))))

for i in range(1, 10):
    filename = 'livello-di-compressione-{}.bz2'.format(i)
    with bz2.BZ2File(filename, 'wb', compresslevel=i) as output:
        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(data)
    os.system('cksum {}'.format(filename))
