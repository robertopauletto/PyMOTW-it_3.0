# socket_echo_server_uds.py

import socket
import sys
import os

server_address = './uds_socket'

# Ci si assicura che il socket non esista
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Crea un socket UDS
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Collega il socket all'indirizzo
print('starting up on {}'.format(server_address))
sock.bind(server_address)

# In ascolto per connessioni in entrata
sock.listen(1)

while True:
    # Attende una connessione
    print('in attesa di una connessione')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Riceve i dati in piccoli segmenti e li ritrasmette
        while True:
            data = connection.recv(16)
            print('ricevuto {!r}'.format(data))
            if data:
                print('reinvio dei dati al client')
                connection.sendall(data)
            else:
                print('nessun dato da', client_address)
                break

    finally:
        # Pulisce la connessione
        connection.close()
