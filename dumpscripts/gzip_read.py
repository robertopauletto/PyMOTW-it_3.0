# gzip_read.py

import gzip
import io

with gzip.open('un_esempio.txt.gz', 'rb') as input_file:
    with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
        print(dec.read())
