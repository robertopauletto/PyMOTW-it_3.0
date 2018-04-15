# traceback_stacksummary.py

import traceback
import sys

from traceback_example import call_function


def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    print(''.join(summary.format()))


print('Chiamata diretta di f():')
f()

print()
print('Chiamata di f() da 3 livelli più in basso:')
call_function(f)
