#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import asyncore
import logging

from asyncore_http_client import HttpClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

clients = [
    HttpClient('http://www.doughellmann.com/PyMOTW/contents.html'),
    HttpClient('http://www.python.org/'),
    ]

loop_counter = 0
while asyncore.socket_map:
    loop_counter += 1
    logging.debug('loop_counter (contatore cicli)=%s', loop_counter)
    asyncore.loop(timeout=1, count=1)