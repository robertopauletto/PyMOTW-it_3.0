# socket_echo_client_uds.py
import socket
import sys

# Crea un socket UDP
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connette il socket alla porta dove è il ascolto il server
server_address = './uds_socket'
print('connessione a {}'.format(server_address))
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

try:

    # Invio dati
    message = b'Ecco il messaggio. Viene restituito.'
    print('in invio {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('ricevuto {!r}'.format(data))

finally:
    print('chiusura socket')
    sock.close()

