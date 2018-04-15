# traceback_print_stack.py

import traceback
import sys

from traceback_example import call_function


def f():
    traceback.print_stack(file=sys.stdout)


print('Chiamata diretta di f():')
f()

print()
print('Chiamata diretta di f() da tre livelli più in basso:')
call_function(f)
