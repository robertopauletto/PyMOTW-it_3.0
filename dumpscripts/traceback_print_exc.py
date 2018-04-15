# traceback_print_exc.py

import traceback
import sys

from traceback_example import produce_exception

print('print_exc() senza eccezioni:')
traceback.print_exc(file=sys.stdout)
print()

try:
    produce_exception()
except Exception as err:
    print('print_exc():')
    traceback.print_exc(file=sys.stdout)
    print()
    print('print_exc(1):')
    traceback.print_exc(limit=1, file=sys.stdout)
