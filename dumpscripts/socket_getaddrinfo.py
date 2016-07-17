#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket

def get_constants(prefix):
    """Crea un dizionario che mappa le costanti del modulo socket ai loro nomi."""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.python.org', 'http'):

    # Spacchetta la tupla response
    family, socktype, proto, canonname, sockaddr = response

    print 'Famiglia        :', families[family]
    print 'Tipo            :', types[socktype]
    print 'Protocollo      :', protocols[proto]
    print 'Nome Canonicoe  :', canonname
    print 'Indirizzo Socket:', sockaddr
    print 