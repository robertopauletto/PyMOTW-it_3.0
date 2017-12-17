# codecs_socket_fail.py

import sys
import socketserver


class Echo(socketserver.BaseRequestHandler):

    def handle(self):
        # Si ottengono alcuni byte e li riverbero al client.
        data = self.request.recv(1024)
        self.request.send(data)
        return


if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0)  # lasciamo assegnare la porta al kernel
    server = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address  # quale porta è stata assegnata?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # non lasciamolo appeso all'uscita
    t.start()

    # Connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Invio dati
    # ERRORE!: prima non sono stati codificati!
    text = 'français'
    len_sent = s.send(text)

    # Recezione di una risposta
    response = s.recv(len_sent)
    print(repr(response))

    # Pulizia
    s.close()
    server.socket.close()
