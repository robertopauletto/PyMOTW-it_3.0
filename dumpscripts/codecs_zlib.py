# codecs_zlib.py

import codecs
import io

from codecs_to_hex import to_hex

buffer = io.BytesIO()
stream = codecs.getwriter('zlib')(buffer)

text = b'abcdefghijklmnopqrstuvwxyz\n' * 50

stream.write(text)
stream.flush()

print('Lunghezza originale:', len(text))
compressed_data = buffer.getvalue()
print('ZIP compresso      :', len(compressed_data))

buffer = io.BytesIO(compressed_data)
stream = codecs.getreader('zlib')(buffer)

first_line = stream.readline()
print('Legge la prima riga:', repr(first_line))

uncompressed_data = first_line + stream.read()
print('Decompressi        :', len(uncompressed_data))
print('Uguali             :', text == uncompressed_data)
