# select_poll_echo_server.py

import select
import socket
import sys
import queue

# Crea un socket TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Collega il socket alla porta
server_address = ('localhost', 10000)
print('in attivazione su {} porta {}'.format(*server_address),
      file=sys.stderr)
server.bind(server_address)

# In ascolto per connessioni in arrivo
server.listen(5)

# Mantiene le code dei messaggi in uscita
message_queues = {}

# Non si blocca per sempre (millisecondi)
TIMEOUT = 1000

# Insiemi di flag comunemente usati
READ_ONLY = (
    select.POLLIN |
    select.POLLPRI |
    select.POLLHUP |
    select.POLLERR
)
READ_WRITE = READ_ONLY | select.POLLOUT

# Imposta il poller
poller = select.poll()
poller.register(server, READ_ONLY)

# Mappa i descrittori di file agli oggetti socket
fd_to_socket = {
    server.fileno(): server,
}

while True:

    # Attende che almeno uno dei socket sia
    # pronto per l'elaborazione
    print('in attesa del prossimo evento', file=sys.stderr)
    events = poller.poll(TIMEOUT)

    for fd, flag in events:

        # Recupera il socket effettivo dal suo descrittore di file
        s = fd_to_socket[fd]

        # Gestione input
        if flag & (select.POLLIN | select.POLLPRI):

            if s is server:
                # UN socket leggibile è pronto
                # per accettare una connessione
                connection, client_address = s.accept()
                print('  connessione', client_address,
                      file=sys.stderr)
                connection.setblocking(0)
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                # Diamo alla connessione una coda per i dati da inviare
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    # Un socket client leggibile ha dei dati
                    print('  recevuti {!r} da {}'.format(
                        data, s.getpeername()), file=sys.stderr,
                    )
                    message_queues[s].put(data)
                    # Si aggiunge un canale di output per la risposta
                    poller.modify(s, READ_WRITE)
                else:
                    # Un risultato vuoto si interpreta come una
                    # connessione chiusa
                    print('  chiusura', client_address,
                          file=sys.stderr)
                    # Si interrompe l'ascolto per in input sulla connessione
                    poller.unregister(s)
                    s.close()

                    # Rimozione della coda dei messaggi.
                    del message_queues[s]
        elif flag & select.POLLHUP:
            # Il client ha interrotto la connessione
            print('  chiusura', client_address, '(HUP)',
                  file=sys.stderr)
            # Si interrompe l'ascolto per in input sulla connessione
            poller.unregister(s)
            s.close()
        elif flag & select.POLLOUT:
            # Il socket è pronto per l'invio dati
            # se ce ne sono da spedire
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                # Nessun messaggio in atttesa, quindi si interrompe
                # la verifica
                print(s.getpeername(), 'coda vuota',
                      file=sys.stderr)
                poller.modify(s, READ_ONLY)
            else:
                print('  inviati {!r} a {}'.format(
                    next_msg, s.getpeername()), file=sys.stderr,
                )
                s.send(next_msg)
        elif flag & select.POLLERR:
            print('  eccezione su', s.getpeername(),
                  file=sys.stderr)
            # Si interrompe l'ascolto per in input sulla connessione
            poller.unregister(s)
            s.close()

            # Rimozione della coda dei messaggi.
            del message_queues[s]
