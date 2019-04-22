# struct_buffers.py

import array
import binascii
import ctypes
import struct

s = struct.Struct('I 2s f')
values = (1, 'ab'.encode('utf-8'), 2.7)
print('Originale  :', values)

print()
print('buffer stringhe ctype')

b = ctypes.create_string_buffer(s.size)
print('Prima       :', binascii.hexlify(b.raw))
s.pack_into(b, 0, *values)
print('Dopo        :', binascii.hexlify(b.raw))
print('Spacchettati:', s.unpack_from(b, 0))

print()
print('array')

a = array.array('b', b'\0' * s.size)
print('Prima        :', binascii.hexlify(a))
s.pack_into(a, 0, *values)
print('Dopo         :', binascii.hexlify(a))
print('Spacchettati:', s.unpack_from(a, 0))
