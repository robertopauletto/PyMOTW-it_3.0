#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import os

parent, child = socket.socketpair()

pid = os.fork()

if pid:
    print 'nel padre, invio messaggio'
    child.close()
    parent.sendall('ping')
    response = parent.recv(1024)
    print 'risposta dal figlio:', response
    parent.close()

else:
    print 'nel figlio, in attesa del messaggio'
    parent.close()
    message = child.recv(1024)
    print 'messaggio dal padre:', message
    child.sendall('pong')
    child.close()