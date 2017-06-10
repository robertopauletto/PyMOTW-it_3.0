# socketserver_threaded.py


socketserver_threaded.py
import threading
import socketserver


class ThreadedEchoRequestHandler(
        socketserver.BaseRequestHandler,
):

    def handle(self):
        # Ripete al client
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = b'%s: %s' % (cur_thread.getName().encode(),
                                data)
        self.request.send(response)
        return


class ThreadedEchoServer(socketserver.ThreadingMixIn,
                         socketserver.TCPServer,
                         ):
    pass


if __name__ == '__main__':
    import socket

    address = ('localhost', 0)  # lasciamo assegnare la porta al kernel
    server = ThreadedEchoServer(address,
                                ThreadedEchoRequestHandler)
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
