# logging_file_example.py

import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

logging.debug('Questo messaggio dovrebbe andare nel file di log')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)

