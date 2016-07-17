import struct
import binascii

values = (1, 'ab', 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Valori originali     :', values
print 'Stringa formattazione:', s.format
print 'Usa                  :', s.size, 'bytes'
print 'Valore Packed        :', binascii.hexlify(packed_data)

