# logging_level_example.py

import logging
import sys

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'avvertimento': logging.WARNING,
    'errore': logging.ERROR,
    'critico': logging.CRITICAL,
}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug('Questo è un messaggio di debug')
logging.info('Questo è un messaggio di informazione')
logging.warning('Questo è un messaggio di avvertimento')
logging.error('Questo è un messaggio di errore')
logging.critical('Questo è un messaggio critico')
