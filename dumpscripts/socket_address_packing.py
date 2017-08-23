# socket_address_packing.py

import binascii
import socket
import struct
import sys

for string_address in ['192.168.1.1', '127.0.0.1']:
    packed = socket.inet_aton(string_address)
    print('Originale    :', string_address)
    print('Impacchettato:', binascii.hexlify(packed))
    print('Spacchettato :', socket.inet_ntoa(packed))
    print()
