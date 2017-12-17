# codecs_socket.py

import sys
import socketserver


class Echo(socketserver.BaseRequestHandler):

    def handle(self):
        """Si ottengono alcuni byte e li si riverbera al client

        Non occorre decoficarli visto che non sono usati.
        """
        data = self.request.recv(1024)
        self.request.send(data)


class PassThrough:

    def __init__(self, other):
        self.other = other

    def write(self, data):
        print('In scrittura:', repr(data))
        return self.other.write(data)

    def read(self, size=-1):
        print('In lettura  :', end=' ')
        data = self.other.read(size)
        print(repr(data))
        return data

    def flush(self):
        return self.other.flush()

    def close(self):
        return self.other.close()


if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0)  # Lasciamo che il kernel ci fornisca una porta
    server = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address  # quale porta ci è stata assegnata?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # don't hang on exit
    t.start()

    # Connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Impacchetta il socket con un lettore e scrittore
    read_file = s.makefile('rb')
    incoming = codecs.getreader('utf-8')(PassThrough(read_file))
    write_file = s.makefile('wb')
    outgoing = codecs.getwriter('utf-8')(PassThrough(write_file))

    # Invio dati
    text = 'français'
    print('In invio    :', repr(text))
    outgoing.write(text)
    outgoing.flush()

    # Receive a response
    response = incoming.read()
    print('Ricevuti:', repr(response))

    # Pulizia
    s.close()
    server.socket.close()

