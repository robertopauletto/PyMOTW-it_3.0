# socket_gethostbyname_ex.py

import socket

HOSTS = [
    'robyp.x10host.com',
    'www.python.org',
    'nonesiste',
]

for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('  Nome Host:', name)
        print('  Alias    :', aliases)
        print('  Indirizzi:', addresses)
    except socket.error as msg:
        print('ERRORE:', msg)
    print()
