# socketserver_forking.py

import os
import socketserver


class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Ripete al client
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = b'%d: %s' % (cur_pid, data)
        self.request.send(response)
        return


class ForkingEchoServer(socketserver.ForkingMixIn,
                        socketserver.TCPServer,
                        ):
    pass


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)  # lasciamo assegnare la porta al kernel
    server = ForkingEchoServer(address,
                               ForkingEchoRequestHandler)
    ip, port = server.server_address  # che porta è stata assegnata?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # non rimane piantato in uscita
    t.start()
    print('Ciclo del server in esecuzione nel processo:', os.getpid())

    # Connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Invio dati
    message = 'Ciao, mondo'.encode()
    print('In invio : {!r}'.format(message))
    len_sent = s.send(message)

    # Ricezione di una risposta
    response = s.recv(1024)
    print('Ricevuto : {!r}'.format(response))

    # Pulizia
    server.shutdown()
    s.close()
    server.socket.close()
