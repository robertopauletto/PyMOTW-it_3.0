# select_echo_multiclient.py

import socket
import sys

messages = [
    'Ecco il messaggio. ',
    'che viene inviato ',
    'in parti.',
]
server_address = ('localhost', 10000)

# Crea un socket TCP/IP
socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

# Connette il socket alla porta dove il server è in ascolto
print('connessione a {} porta {}'.format(*server_address),
      file=sys.stderr)
for s in socks:
    s.connect(server_address)

for message in messages:
    outgoing_data = message.encode()

    # Invia messaggi ad entrambi i socket
    for s in socks:
        print('{}: in invio {!r}'.format(s.getsockname(),
                                        outgoing_data),
              file=sys.stderr)
        s.send(outgoing_data)

    # Legge le risposte da  entrambi i socket
    for s in socks:
        data = s.recv(1024)
        print('{}: ricevuto {!r}'.format(s.getsockname(),
                                         data),
              file=sys.stderr)
        if not data:
            print('chiusura socket', s.getsockname(),
                  file=sys.stderr)
            s.close()
