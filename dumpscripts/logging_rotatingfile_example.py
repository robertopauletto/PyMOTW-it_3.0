#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Impostazione di un logger specifico con il livello di output desiderato
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Aggiunta dell'handler dei messaggi di log al logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                               maxBytes=20,
                                               backupCount=5,
                                               )
my_logger.addHandler(handler)

# Registrazione di qualche messaggio
for i in range(20):
    my_logger.debug('i = %d' % i)

# Visualizzazione dei file che sono stati creati
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
    print filename    
