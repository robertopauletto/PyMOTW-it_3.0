# socket_echo_server_any.py

import socket
import sys

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connette il socket alla porta sul server passata dal chiamante
server_address = ('', 10000)
sock.bind(server_address)
print('in avvio su {} porta {}'.format(*server_address))
sock.listen(1)

while True:
    print('in attesa di una connessione')
    connection, client_address = sock.accept()
    try:
        print('client connesso:', client_address)
        while True:
            data = connection.recv(16)
            print('ricevuto {!r}'.format(data))
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
