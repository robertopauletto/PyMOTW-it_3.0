# ipaddress_networks.py

import ipaddress

NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    print('          è privato:', net.is_private)
    print('          broadcast:', net.broadcast_address)
    print('          compresso:', net.compressed)
    print('   con maschera net:', net.with_netmask)
    print('  con maschera host:', net.with_hostmask)
    print('   numero indirizzi:', net.num_addresses)
    print()
