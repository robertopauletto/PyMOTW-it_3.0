# gzip_seek.py

import gzip

with gzip.open('un_esempio.txt.gz', 'rb') as input_file:
    print('Tutto il file:')
    all_data = input_file.read()
    print(all_data)

    expected = all_data[5:15]

    # si riporta ad inizio file
    input_file.seek(0)

    # avanti di 5 byte
    input_file.seek(5)
    print('A partire dalla posizione 5 per 10 byte:')
    partial = input_file.read(10)
    print(partial)

    print()
    print(expected == partial)
