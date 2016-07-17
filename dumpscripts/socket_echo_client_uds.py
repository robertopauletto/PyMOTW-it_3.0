#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

# Crea un socket UDP
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connette il socket alla porta dove è il ascolot il server
server_address = './uds_socket'
print >>sys.stderr, 'connessione a %s' % server_address
try:
    sock.connect(server_address)
except socket.error, msg:
    print >>sys.stderr, msg
    sys.exit(1)


try:

    # Invio dati
    message = 'Questo è il messaggio. Verrà ripetuto'
    print >>sys.stderr, 'in invio "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)    
        print >>sys.stderr, 'ricevuto "%s"' % data

finally:
    print >>sys.stderr, 'chiusura del socket'
    sock.close()