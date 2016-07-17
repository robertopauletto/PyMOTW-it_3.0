#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )

logging.debug('Questo messaggio dovrebbe andare nel file di log')

f = open(LOG_FILENAME, 'rt')
try:
    body = f.read()
finally:
    f.close()

print 'FILE:'
print body