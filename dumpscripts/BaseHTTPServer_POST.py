#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

class PostHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # Elabora i dati ricevuti nel form
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Dati form:\n')

        # Rimanda le informazioni su ciò che era stato passato nel form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # Il campo contiene un file che è stato inviato
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write('\tInviato %s as "%s" (%d bytes)\n' % \
                        (field, field_item.filename, file_len))
            else:
                # Valori normali nel form
                self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Server in esecuzione, usare <Ctrl-C> per interrompere'
    server.serve_forever()