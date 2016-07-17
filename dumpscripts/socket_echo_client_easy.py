#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

def get_constants(prefix):
    """Crea un dizonario che mappa le costanti del modulo socket ai loro nomi"""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Crea un socket TCP/IP
sock = socket.create_connection(('localhost', 10000))

print >>sys.stderr, 'Famiglia  :', families[sock.family]
print >>sys.stderr, 'Tipo      :', types[sock.type]
print >>sys.stderr, 'Protocollo:', protocols[sock.proto]
print >>sys.stderr

try:
    
    # Invio data
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
    print >>sys.stderr, 'chiusura del socket'
    sock.close()