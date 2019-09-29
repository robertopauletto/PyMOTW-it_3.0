# ipaddress_interfaces.py

import ipaddress


ADDRESSES = [
    '10.9.0.6/24',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64',
]


for ip in ADDRESSES:
    iface = ipaddress.ip_interface(ip)
    print('{!r}'.format(iface))
    print('rete:\n  ', iface.network)
    print('ip:\n  ', iface.ip)
    print('IP con prefisso di lunghezza:\n  ', iface.with_prefixlen)
    print('maschera di rete:\n  ', iface.with_netmask)
    print('maschera host:\n  ', iface.with_hostmask)
    print()
