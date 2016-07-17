#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import binascii
import socket
import struct
import sys

string_address = sys.argv[1]
packed = socket.inet_aton(string_address)

print 'Originale:', string_address
print 'Packed   :', binascii.hexlify(packed)
print 'Unpacked :', socket.inet_ntoa(packed)