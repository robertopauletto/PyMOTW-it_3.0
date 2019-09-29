# ipaddress_addresses.py

import binascii
import ipaddress


ADDRESSES = [
    '10.9.0.6',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for ip in ADDRESSES:
    addr = ipaddress.ip_address(ip)
    print('{!r}'.format(addr))
    print('             versione IP:', addr.version)
    print('               è privato:', addr.is_private)
    print('  formato pacchettizzato:', binascii.hexlify(addr.packed))
    print('                  intero:', int(addr))
    print()
