# selectors_echo_client.py

import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True
outgoing = [
    b'Viene ripetuto.',
    b'Questo messaggio.  ',
]
bytes_sent = 0
bytes_received = 0

# La connessione è una operazione bloccante, quindi si chiama setblocking()
# dopo il ritorno
server_address = ('localhost', 10000)
print('connessione a {} porta {}'.format(*server_address))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock.setblocking(False)

# Imposta il selettore per verificare quando il socket è pronto
# per inviare dati oppure per verificare se ci sono dati da leggere
mysel.register(
    sock,
    selectors.EVENT_READ | selectors.EVENT_WRITE,
)

while keep_running:
    print('in attesa di I/O')
    for key, mask in mysel.select(timeout=1):
        connection = key.fileobj
        client_address = connection.getpeername()
        print('client({})'.format(client_address))

        if mask & selectors.EVENT_READ:
            print('  pronto per legger')
            data = connection.recv(1024)
            if data:
                # Un socket client leggibile ha dati
                print('  ricevuti {!r}'.format(data))
                bytes_received += len(data)

            # Interpreta un risultato vuoto come connessione chiusa
            # e chiude anche quando si è ricevuta una copia di tutti
            # i dati inviati.
            keep_running = not (
                data or
                (bytes_received and
                 (bytes_received == bytes_sent))
            )

        if mask & selectors.EVENT_WRITE:
            print('  pronto per scrivere')
            if not outgoing:
                # I messaggi sono esauriti, quindi non serve più
                # scrivere qualcosa. Si modifica la registrazione per
                # consentirci di leggere le risposte dal server.
                print('  si passa a sola lettura')
                mysel.modify(sock, selectors.EVENT_READ)
            else:
                # Invia il messaggio successivo
                next_msg = outgoing.pop()
                print('  in invio {!r}'.format(next_msg))
                sock.sendall(next_msg)
                bytes_sent += len(next_msg)

print('terminato')
mysel.unregister(connection)
connection.close()
mysel.close()
