# array_string.py

import array
import binascii

s = b"Questo e' un array."
a = array.array('b', s)

print('Come stringa di byte:', s)
print('Come array         :', a)
print('Come esadecimale   : hex        :', binascii.hexlify(a))
