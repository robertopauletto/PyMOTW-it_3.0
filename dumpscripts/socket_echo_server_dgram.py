#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

# Crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Attacca il socket alla porta
server_address = ('localhost', 10000)
print >>sys.stderr, 'in avvio su %s porta %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nin attesa di ricevere un messaggio'
    data, address = sock.recvfrom(4096)
    
    print >>sys.stderr, 'recevuti %s byte da %s' % (len(data), address)
    print >>sys.stderr, data
    
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'ritornati %s byte a %s' % (sent, address)