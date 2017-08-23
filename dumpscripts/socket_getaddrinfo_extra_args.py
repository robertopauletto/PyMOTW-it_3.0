# socket_getaddrinfo_extra_args.py

import socket


def get_constants(prefix):
    """Crea un dizionario che mappa le costanti del modulo socket
    ai loro nomi.
    """
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

responses = socket.getaddrinfo(
    host='www.python.org',
    port='http',
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=socket.IPPROTO_TCP,
    flags=socket.AI_CANONNAME,
)

for response in responses:
    # Spacchetta la tupla response
    family, socktype, proto, canonname, sockaddr = response

    print('Famiglia      :', families[family])
    print('Tipo          :', types[socktype])
    print('Protocollo    :', protocols[proto])
    print('Nome Canonico :', canonname)
    print('Indir. socket :', sockaddr)
    print()
