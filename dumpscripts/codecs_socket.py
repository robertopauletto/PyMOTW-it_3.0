#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import SocketServer


class Echo(SocketServer.BaseRequestHandler):

    def handle(self):
        # Si ottengono alcuni byte e li si riverbera al client.  There is
        # Non occorre decoficarli visto che non sono usati.
        data = self.request.recv(1024)
        self.request.send(data)
        return


class PassThrough(object):

    def __init__(self, other):
        self.other = other

    def write(self, data):
        print 'In scrittura :', repr(data)
        return self.other.write(data)

    def read(self, size=-1):
        print 'In lettura :',
        data = self.other.read(size)
        print repr(data)
        return data

    def flush(self):
        return self.other.flush()

    def close(self):
        return self.other.close()
    

if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0) # Lasciamo che il kernel ci fornisca una porta
    server = SocketServer.TCPServer(address, Echo)
    ip, port = server.server_address # scopriamo quale porta ci è stata assegnata

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # non lo lasciamo appeso all'uscita
    t.start()

    # Connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Incapsula il socket in un lettore e scrittore
    incoming = codecs.getreader('utf-8')(PassThrough(s.makefile('r')))
    outgoing = codecs.getwriter('utf-8')(PassThrough(s.makefile('w')))

    # Invia i dati
    text = u'pi: π'
    print 'Inviati :', repr(text)
    outgoing.write(text)
    outgoing.flush()

    # Riceve una risposta
    response = incoming.read()
    print 'Ricevuti:', repr(response)

    # Pulizia
    s.close()
    server.socket.close()