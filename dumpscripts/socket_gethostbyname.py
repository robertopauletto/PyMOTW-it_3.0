# socket_gethostbyname.py

import socket

HOSTS = [
    'robyp.x10host.com',
    'www.python.org',
    'nonesiste',
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))
