# traceback_framesummary.py

import traceback
import sys

from traceback_example import call_function

template = (
    '{fs.filename:<26}:{fs.lineno}:{fs.name}:\n'
    '    {fs.line}'
)


def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    for fs in summary:
        print(template.format(fs=fs))


print('Chiamata diretta di f():')
f()

print()
print('Chiamata di f() da tre livelli più in basso:')
call_function(f)
