#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

# Crea un socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connette il socket alla porta sul server passata dal chiamante caller
server_address = (sys.argv[1], 10000)
print >>sys.stderr, 'connessione a %s porta %s' % server_address
sock.connect(server_address)

try:
    
    message = 'Questo è il messaggio. Verrà ripetuto.'
    print >>sys.stderr, 'invio "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'ricevuto "%s"' % data

finally:
    sock.close()