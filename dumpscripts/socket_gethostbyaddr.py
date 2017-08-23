# socket_gethostbyaddr.py

import socket

hostname, aliases, addresses = socket.gethostbyaddr('198.91.81.4')

print('None host:', hostname)
print('Alias    :', aliases)
print('Indirizzi:', addresses)
