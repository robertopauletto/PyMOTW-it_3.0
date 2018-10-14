# bz2_file_write.py

import bz2
import io
import os

data = 'Il contenuto del file esempio va qui.\n'

with bz2.BZ2File('esempio.bz2', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write(data)

os.system('file esempio.bz2')
