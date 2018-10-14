# sys_stdio.py

import sys

print('STATO: In lettura da stdin', file=sys.stderr)

data = sys.stdin.read()

print('STATO: Scrittura dati verso stdout', file=sys.stderr)

sys.stdout.write(data)
sys.stdout.flush()

print('STATO: Fatto', file=sys.stderr)
