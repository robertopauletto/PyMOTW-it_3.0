# select_echo_slow_client.py

import socket
import sys
import time

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connette il socket alla porta dove il server è in ascolto
server_address = ('localhost', 10000)
print('connessione a {} porta {}'.format(*server_address),
      file=sys.stderr)
sock.connect(server_address)

time.sleep(1)

messages = [
    'Prima parte del messaggio.',
    'Seconda parte del messaggio.',
]
amount_expected = len(''.join(messages))

try:

    # Invio dati
    for message in messages:
        data = message.encode()
        print('in invio {!r}'.format(data), file=sys.stderr)
        sock.sendall(data)
        time.sleep(1.5)

    # Ricerca della risposta
    amount_received = 0

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('recevuti {!r}'.format(data), file=sys.stderr)

finally:
    print('chiusura socket', file=sys.stderr)
    sock.close()
