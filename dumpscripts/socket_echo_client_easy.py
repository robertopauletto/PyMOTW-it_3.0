# socket_echo_client_easy.py

import socket
import sys


def get_constants(prefix):
    """Crea un dizionareio che mappa le costanti del modulo socke
    ai propri nomi.
    """
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Crea un socket TCP/IP
sock = socket.create_connection(('localhost', 10000))

print('Famiglia  :', families[sock.family])
print('Tipo      :', types[sock.type])
print('Protocollo:', protocols[sock.proto])
print()

try:

    # Invio dati
    message = b'Ecco il messaggio. Viene restituito.'
    print('invio di {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('ricevuto {!r}'.format(data))

finally:
    print('chiusura del socket')
    sock.close()
