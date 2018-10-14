# gzip_write.py

import gzip
import io
import os

outfilename = 'un_esempio.txt.gz'
with gzip.open(outfilename, 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write('I contenuti del file di esempio vanno qui.\n')

print(outfilename, 'contiene', os.stat(outfilename).st_size,
      'byte')
os.system('file -b --mime {}'.format(outfilename))
