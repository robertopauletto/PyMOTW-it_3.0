# socket_multicast_receiver.py

import socket
import struct
import sys

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Crea il socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Collega l'indirizzo del server
sock.bind(server_address)

# Dice al sistema operativo di aggiungere il socket al
# gruppo multicast su tutte le interfacce.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq)

# Receive/respond loop
while True:
    print('\nin attesa di ricevere messaggi')
    data, address = sock.recvfrom(1024)

    print('ricevuti{} bytes da {}'.format(
        len(data), address))
    print(data)

    print('invio riconoscimento a', address)
    sock.sendto(b'ack', address)
