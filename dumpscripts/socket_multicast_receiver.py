#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import struct
import sys

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Dice al sistema opearativo di aggiungere il socket al gruppo multicast
# su tutte le interfacce
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Ciclo di ricezione/risposta
while True:
    print >>sys.stderr, '\nIn attesa di ricevere un messaggio'
    data, address = sock.recvfrom(1024)
    
    print >>sys.stderr, 'recevuti %s byte da %s' % (len(data), address)
    print >>sys.stderr, data

    print >>sys.stderr, 'invio riconoscimento a', address
    sock.sendto('ack', address)