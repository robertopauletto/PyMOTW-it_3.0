#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import asyncore
import logging
import socket

from asynchat_echo_server import EchoServer
from asynchat_echo_client import EchoClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

address = ('localhost', 0) # lasciamo che sia il kernel a fornirci una porta
server = EchoServer(address)
ip, port = server.address # scopriamo quale porta ci è stata assegnata

message_data = open('lorem.txt', 'r').read()
client = EchoClient(ip, port, message=message_data)

asyncore.loop()