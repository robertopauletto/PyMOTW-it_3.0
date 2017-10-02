# pathlib_read_write.py

import pathlib

f = pathlib.Path('esempio.txt')

f.write_bytes('Questo è il contenuto'.encode('utf-8'))

with f.open('r', encoding='utf-8') as handle:
    print('lettura open(): {!r}'.format(handle.read()))

print('read_text(): {!r}'.format(f.read_text('utf-8')))
