#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket

hostname, aliases, addresses = socket.gethostbyaddr('192.168.254.2')

print 'Hostname :', hostname
print 'Aliases  :', aliases
print 'Addresses:', addresses