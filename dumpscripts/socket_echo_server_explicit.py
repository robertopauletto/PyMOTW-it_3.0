#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attacca il socket all'indirizzo ricevuto da riga di comando
server_name = sys.argv[1]
server_address = (server_name, 10000)
print >>sys.stderr, 'in avvio su %s porta %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'in attesa di una connessione'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connesso:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'ricevuto "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()