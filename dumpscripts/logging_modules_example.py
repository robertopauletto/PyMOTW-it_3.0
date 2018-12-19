# logging_modules_example.py

import logging

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('Questo messaggio viene da un modulo')
logger2.warning('Questo viene da un altro modulo')
