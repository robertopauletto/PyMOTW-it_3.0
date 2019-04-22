# struct_endianness.py

import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
print('Valori originali    :', values)

endianness = [
    ('@', 'native, native'),
    ('=', 'native, standard'),
    ('<', 'little-endian'),
    ('>', 'big-endian'),
    ('!', 'network'),
]

for code, name in endianness:
    s = struct.Struct(code + ' I 2s f')
    packed_data = s.pack(*values)
    print()
    print('Formato stringa     :', s.format, 'per', name)
    print('Usa                 :', s.size, 'byte')
    print('Valore impacchettato:', binascii.hexlify(packed_data))
    print('Valore spacchettato :', s.unpack(packed_data))
