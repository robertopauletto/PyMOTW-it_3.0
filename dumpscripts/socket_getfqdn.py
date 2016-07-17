#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket

for host in [ 'homer', 'www' ]:
    print '%6s : %s' % (host, socket.getfqdn(host))