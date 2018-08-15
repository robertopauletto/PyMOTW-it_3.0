# zlib_compresslevel.py

import zlib

input_data = b'Del testo ripetuto.\n' * 1024
template = '{:>7}  {:>10}'

print(template.format('Livello', 'Dimensione'))
print(template.format('-------', '----------'))

for i in range(0, 10):
    data = zlib.compress(input_data, i)
    print(template.format(i, len(data)))
