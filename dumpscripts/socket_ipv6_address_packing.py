#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Collega il socket alla porta
server_address = ('localhost', 10000)
print >>sys.stderr, 'in avvio sulla porta %s  %s' % server_address
sock.bind(server_address)