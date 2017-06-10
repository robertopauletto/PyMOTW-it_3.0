# http_server_POST.py

import cgi
from http.server import BaseHTTPRequestHandler
import io


class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        # Inizio della risposta
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )

        out.write('Client: {}\n'.format(self.client_address))
        out.write('User-agent: {}\n'.format(
            self.headers['user-agent']))
        out.write('Percorso: {}\n'.format(self.path))
        out.write('Dati del form:\n')

        # Ritorna le informazioni di ciò che era stato inviato nel form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # Il campo contiene un file inviato
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                out.write(
                    '\tUploaded {} as {!r} ({} bytes)\n'.format(
                        field, field_item.filename, file_len)
                )
            else:
                # Valori del normali
                out.write('\t{}={}\n'.format(
                    field, form[field].value))

        # Disconnette il wrapper di codifica dal buffer sottostante
        # in modo che l'eliminazione del wrapper non chiuda
        # il socket, che è ancora in uso dal server.
        out.detach()


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print('Server in esecuzione, usare <Ctrl-C> per terminare')
    server.serve_forever()
