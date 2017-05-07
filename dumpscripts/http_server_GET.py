# http_server_GET.py

from http.server import BaseHTTPRequestHandler
from urllib import parse


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        message_parts = [
            'VALORI DEL CLIENT:',
            'indirizzi client={} ({})'.format(
                self.client_address,
                self.address_string()),
            'comando={}'.format(self.command),
            'percorso={}'.format(self.path),
            'percorso reale={}'.format(parsed_path.path),
            'query={}'.format(parsed_path.query),
            'versione richiesta={}'.format(self.request_version),
            '',
            'VALORI DEL SERVER:',
            'versione server={}'.format(self.server_version),
            'versione sys={}'.format(self.sys_version),
            'versione protocollo={}'.format(self.protocol_version),
            '',
            'INTESTAZIONI RICEVUTE:',
        ]
        for name, value in sorted(self.headers.items()):
            message_parts.append(
                '{}={}'.format(name, value.rstrip())
            )
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Avvio del server, usare <Ctrl-C> per interrompere')
    server.serve_forever()
