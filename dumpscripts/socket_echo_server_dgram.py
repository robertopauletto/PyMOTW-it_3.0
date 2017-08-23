# socket_echo_server_dgram.py

import socket
import sys

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connette il socket alla porta sul server passata dal chiamante
server_address = ('', 10000)
sock.bind(server_address)
print('in avvio su {} porta {}'.format(*server_address))

while True:
    print('in attesa di una connessione')
    data, address = sock.recvfrom(4096)

    print('ricevuti {} byte da {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('ritornati {} byte a {}'.format(sent, address))
