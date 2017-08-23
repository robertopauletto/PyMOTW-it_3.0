# socket_echo_client_explicit.py

import socket
import sys

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connette il socket alla porta sul server passata dal chiamante
server_address = (sys.argv[1], 10000)
print('connessione a {} porta {}'.format(*server_address))
sock.connect(server_address)

try:

    message = b'Ecco il messaggio. Viene restituito'
    print('inviato {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('ricevuto {!r}'.format(data))

finally:
    sock.close()
