# struct_pack.py

import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print('Valori originali    :', values)
print('Formato stringa     :', s.format)
print('Usa                 :', s.size, 'byte')
print('Valore impacchettato:', binascii.hexlify(packed_data))
