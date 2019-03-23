# getpass_noterminal.py

import getpass
import sys


if sys.stdin.isatty():
    p = getpass.getpass('Si sta usando getpass: ')
else:
    print('Si sta usando readline')
    p = sys.stdin.readline().rstrip()

print('Letto: ', p)
