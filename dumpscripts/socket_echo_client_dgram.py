#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

# Crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'Questo è il messaggio. Verrà ripetuto'

try:

    # Invio dati
    print >>sys.stderr, 'in invio "%s"' % message
    sent = sock.sendto(message, server_address)

    # Recezione risposta
    print >>sys.stderr, 'in attesa di ricezione'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'ricevuto "%s"' % data

finally:
    print >>sys.stderr, 'chiusura del socket'
    sock.close()