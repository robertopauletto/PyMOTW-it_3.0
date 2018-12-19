# logging_capture_warnings.py

import logging
import warnings

logging.basicConfig(
    level=logging.INFO,
)

warnings.warn('Questo avvertimento non viene registrato')

logging.captureWarnings(True)

warnings.warn('Questo avvertimento viene registrato')
