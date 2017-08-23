# socket_echo_client_dgram.py

import socket
import sys

# Crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'Ecco il messaggio. Viene restituito.'

try:

    # Invio datif
    print('in invio {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Ricezione risposta
    print('in attesa di ricevere')
    data, server = sock.recvfrom(4096)
    print('ricevuti {!r}'.format(data))

finally:
    print('chiusura socket')
    sock.close()
