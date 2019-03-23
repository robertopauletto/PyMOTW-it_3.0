# warnings_once.py

import warnings

warnings.simplefilter('once', UserWarning)

warnings.warn('Questo è un avvertimento!')
warnings.warn('Questo è un avvertimento!')
warnings.warn('Questo è un avvertimento!')
