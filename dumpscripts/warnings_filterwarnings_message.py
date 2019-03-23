# warnings_filterwarnings_message.py

import warnings

warnings.filterwarnings('ignore', '.*non mostrare.*',)

warnings.warn('Mostra questo messaggio')
warnings.warn('Non mostrare questo messaggio')
