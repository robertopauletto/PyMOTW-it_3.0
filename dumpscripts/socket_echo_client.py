#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

# Crea un socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connette il socket alla porta dove è in ascolto il  server
server_address = ('localhost', 10000)
print >>sys.stderr, 'connessione a %s porta %s' % server_address
sock.connect(server_address)

try:
    
    # Invio dati
    message = 'Questo è il messaggio. Verrà ripetuto.'
    print >>sys.stderr, 'invio "%s"' % message
    sock.sendall(message)

    # Cerca la risposta
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'ricevuto "%s"' % data

finally:
    print >>sys.stderr, 'chiusura del socket'
    sock.close()