# socket_multicast_sender.py

import socket
import struct
import sys

message = b'dati molto importanti'
multicast_group = ('224.3.29.71', 10000)

# Crea il socket datagramm
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Imposta un timeout così che il socket non blocchi
# indefinitivamente quando tenta di ricevere dati.
sock.settimeout(0.2)

# Imposta il time-to-live per i messaggi ad 1 in modo che non superino
# il segmento di rete locale
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:

    # Invia dati al gluppo multicast
    print('in invio {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)

    # Cerca le risposte da tutti i destinatari
    while True:
        print('in attesa di ricevere')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('tempo esaurito, non ci sono più risposte')
            break
        else:
            print('ricevuti {!r} da {}'.format(
                data, server))

finally:
    print('chiusura socket')
    sock.close()

