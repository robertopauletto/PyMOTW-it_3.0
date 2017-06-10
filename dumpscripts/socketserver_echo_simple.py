# socketserver_echo_simple.py

import socketserver


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        self.request.send(data)
        return


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)  # lasciamo assegnare la porta al kernel
    server = socketserver.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address  # che porta è stata assegnata?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # non rimane piantato in uscita
    t.start()

    # Connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Invio dati
    message = 'Ciao, mondo'.encode()
    print('In invio : {!r}'.format(message))
    len_sent = s.send(message)

    # Ricezione di una risposta
    response = s.recv(len_sent)
    print('Ricevuto : {!r}'.format(response))

    # Pulizia
    server.shutdown()
    s.close()
    server.socket.close()
