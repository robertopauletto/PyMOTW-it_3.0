# gzip_writelines.py

import gzip
import io
import itertools
import os

with gzip.open('un_esempio_con_righe.txt.gz', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(
            itertools.repeat('La stessa riga, ripetuta 10 volte.\n',
                             10)
        )

os.system('gunzip -c un_esempio_con_righe.txt.gz')
