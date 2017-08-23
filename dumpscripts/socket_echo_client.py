# socket_echo_client.py

import socket
import sys

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connette il socket alla porta alla quale il server è in ascolto
server_address = ('localhost', 10000)
print('connessione a {} porta {}'.format(*server_address))
sock.connect(server_address)

try:

    # Invio dati
    message = b'Ecco il messaggio. Viene restituito.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Cerca una risposta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('ricevuti {!r}'.format(data))

finally:
    print('chiusura socket')
    sock.close()
