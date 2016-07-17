import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem)
all_at_once = h.hexdigest()

def chunkize(size, text):
    "Restituisce parti del testo con incrementi in base alla dimensione di size."
    start = 0
    while start < len(text):
        chunk = text[start:start+size]
        yield chunk
        start += size
        return

h = hashlib.md5()
for chunk in chunkize(64, lorem):
    h.update(chunk)
    line_by_line = h.hexdigest()

print 'Tutto insieme:', all_at_once
print 'Riga per riga:', line_by_line
print 'Uguale       :', (all_at_once == line_by_line)
                                                    
