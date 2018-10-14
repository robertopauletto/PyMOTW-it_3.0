# bz2_file_seek.py

import bz2
import contextlib

with bz2.BZ2File('esempio.bz2', 'rb') as input:
    print('Tutto il file:')
    all_data = input.read()
    print(all_data)

    expected = all_data[5:15]

    # mi porto all'inizio
    input.seek(0)

    # mi sposto in avanti di 5 byte
    input.seek(5)
    print('A partire dalla posizione 5 per 10 byte:')
    partial = input.read(10)
    print(partial)

    print()
    print(expected == partial)
