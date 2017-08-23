# socket_socketpair.py

import socket
import os

parent, child = socket.socketpair()

pid = os.fork()

if pid:
    print('nel genitore, invio messaggio')
    child.close()
    parent.sendall(b'ping')
    response = parent.recv(1024)
    print('risposta dal figlio:', response)
    parent.close()

else:
    print('nel figlio, in attesa del messagio')
    parent.close()
    message = child.recv(1024)
    print('messaggio dal genitore:', message)
    child.sendall(b'pong')
    child.close()

