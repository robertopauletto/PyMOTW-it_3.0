# traceback_tracebackexception.py

import traceback
import sys

from traceback_example import produce_exception

print('senza eccezioni:')
exc_type, exc_value, exc_tb = sys.exc_info()
tbe = traceback.TracebackException(exc_type, exc_value, exc_tb)
print(''.join(tbe.format()))

print('\ncon eccezioni:')
try:
    produce_exception()
except Exception as err:
    exc_type, exc_value, exc_tb = sys.exc_info()
    tbe = traceback.TracebackException(
        exc_type, exc_value, exc_tb,
    )
    print(''.join(tbe.format()))

    print('\nsolo eccezioni:')
    print(''.join(tbe.format_exception_only()))
