# socket_ipv6_address_packing.py

import binascii
import socket
import struct
import sys

string_address = '2002:ac10:10a:1234:21e:52ff:fe74:40e'
packed = socket.inet_pton(socket.AF_INET6, string_address)

print('Originale    :', string_address)
print('Impacchettato:', binascii.hexlify(packed))
print('Spacchettato :', socket.inet_ntop(socket.AF_INET6, packed))
