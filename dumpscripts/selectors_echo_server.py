# selectors_echo_server.py

import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True


def read(connection, mask):
    "Callback for eventi di lettura"
    global keep_running

    client_address = connection.getpeername()
    print('letti({})'.format(client_address))
    data = connection.recv(1024)
    if data:
        # Un socket client leggibile ha dati
        print('  ricevuti {!r}'.format(data))
        connection.sendall(data)
    else:
        # Interpreta un risultato vuoto come connessione chiusa
        print('  chiusura')
        mysel.unregister(connection)
        connection.close()
        # Dice al ciclo principale di fermarsi
        keep_running = False


def accept(sock, mask):
    "Callback per nuove connessioni"
    new_connection, addr = sock.accept()
    print('accetta({})'.format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)


server_address = ('localhost', 10000)
print('In esecuzione su {} porta {}'.format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

mysel.register(server, selectors.EVENT_READ, accept)

while keep_running:
    print('in attesa di I/O')
    for key, mask in mysel.select(timeout=1):
        callback = key.data
        callback(key.fileobj, mask)

print('terminato')
mysel.close()
