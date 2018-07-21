# hashlib_update.py

import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
all_at_once = h.hexdigest()


def chunkize(size, text):
    "Ritorna parti di testo con incrementi in base alla dimensione."
    start = 0
    while start < len(text):
        chunk = text[start:start + size]
        yield chunk
        start += size
    return


h = hashlib.md5()
for chunk in chunkize(64, lorem.encode('utf-8')):
    h.update(chunk)
line_by_line = h.hexdigest()

print('Tutto in una volta:', all_at_once)
print('Riga per Riga     :', line_by_line)
print('Verifica          :', (all_at_once == line_by_line))
