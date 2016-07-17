#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import struct
import sys

message = 'dati molto importanti'
multicast_group = ('224.3.29.71', 10000)

# Crea il socket datagram
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Imposta un timeout in modo che il socket non blocchi indefinitivamente mentre
# tenta di ricevere dati
sock.settimeout(0.2)

# Imposta il time-to-live per i messaggi ad 1 in modo che non vadano
# oltre il segmento locale di rete.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:

    # Invia dati al gruppo multicast
    print >>sys.stderr, 'in invio "%s"' % message
    sent = sock.sendto(message, multicast_group)

    # Cerca le risposte da tutti i ricettori
    while True:
        print >>sys.stderr, 'in attesa di ricezione'
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print >>sys.stderr, 'raggiunto time out, non ci sono più risposte'
            break
        else:
            print >>sys.stderr, 'recevuto "%s" from %s' % (data, server)

finally:
    print >>sys.stderr, 'chiusura socket'
    sock.close()