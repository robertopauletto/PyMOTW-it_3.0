# select_echo_server.py

import select
import socket
import sys
import queue


# Crea un socket TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Collega il socket alola  port
server_address = ('localhost', 10000)
print('in partenza sulla porta {} {}'.format(*server_address),
      file=sys.stderr)
server.bind(server_address)

# In ascolto per connessioni in arrivo
server.listen(5)

# Sockets dai quali ci si attende una lettura
inputs = [server]

# Sockets verso i quali ci si prevede di scrivere
outputs = []

# Code di messaggio in uscita (socket:Queue)
message_queues = {}

timeout = 1.0

while inputs:

    # Attende che almeno uno dei socket sia
    # pronto per l'elaborazione
    print('in attesa dell\'evento successivo', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs,
                                                    outputs,
                                                    inputs,
                                                    timeout)

    if not (readable or writable or exceptional):
        print('  tempo esaurito, si eseguono altri compiti',
              file=sys.stderr)
        continue

# Gestione input
    for s in readable:

        if s is server:
            # Un socket "leggibile" è pronto ad accettare una connessione
            connection, client_address = s.accept()
            print('  connessione da', client_address,
                  file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # Fornisce alla connessione una coda per i dati che si
            # vogliono inviare
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # Un socket client leggibile ha dati
                print('  ricevuti {!r} da {}'.format(
                    data, s.getpeername()), file=sys.stderr,
                )
                message_queues[s].put(data)
                # Aggiunge al canale in output per la risposta
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpreta un risultato vuoto come connessione chiusa
                print('  chiusura', client_address,
                      file=sys.stderr)
                # Interrompe l'ascolto per input sulla connessione
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Rimuove la coda di messaggi
                del message_queues[s]

    # Gestione output
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # Non ci son omessaggi in attesa, quindi si interrompe la verifica
            # di "scrivibilità"
            print('  ', s.getpeername(), 'coda vuota',
                  file=sys.stderr)
            outputs.remove(s)
        else:
            print('  in invio {!r} verso {}'.format(next_msg,
                                                    s.getpeername()),
                  file=sys.stderr)
            s.send(next_msg)

    # Gestione delle "condizioni di eccezione"
    for s in exceptional:
        print('condizione di eccezione', s.getpeername(),
              file=sys.stderr)
        # Interrompe l'ascolto in input per la connessione
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Rimuove la coda di messaggio
        del message_queues[s]
