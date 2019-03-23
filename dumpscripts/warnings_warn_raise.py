# warnings_warn_raise.py

import warnings

warnings.simplefilter('error', UserWarning)

print("Prima dell'avvertimento")
warnings.warn('Questo è un messaggio di avvertimento')
print("Dopo l'avvertimento")
