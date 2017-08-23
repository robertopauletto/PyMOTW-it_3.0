# socket_echo_server.py

import socket
import sys

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Collega il socket alla porta
server_address = ('localhost', 10000)
print('In avvio su {} porta {}'.format(*server_address))
sock.bind(server_address)

# In ascolto per una connessione in arrivo
sock.listen(1)

while True:
    # In attesa di una connessioe
    print('in attesa di una connessioe')
    connection, client_address = sock.accept()
    try:
        print('connessione da', client_address)

        # Riceve i dati in piccoli segmenti e li ritrasmette
        while True:
            data = connection.recv(16)
            print('ricevuti {!r}'.format(data))
            if data:
                print('reinvio dei dati al client')
                connection.sendall(data)
            else:
                print('non ci sono più dati da', client_address)
                break

    finally:
        # Pulisce la connessione
        connection.close()
