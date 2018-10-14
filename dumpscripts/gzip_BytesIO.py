# gzip_BytesIO.py

import gzip
from io import BytesIO
import binascii

uncompressed_data = b'La stessa riga, ripetuta 10 volte.\n' * 10
print('NON COMPRESSO:', len(uncompressed_data))
print(uncompressed_data)

buf = BytesIO()
with gzip.GzipFile(mode='wb', fileobj=buf) as f:
    f.write(uncompressed_data)

compressed_data = buf.getvalue()
print('COMPRESSO:', len(compressed_data))
print(binascii.hexlify(compressed_data))

inbuffer = BytesIO(compressed_data)
with gzip.GzipFile(mode='rb', fileobj=inbuffer) as f:
    reread_data = f.read(len(uncompressed_data))

print('\nRILETTURA:', len(reread_data))
print(reread_data)
