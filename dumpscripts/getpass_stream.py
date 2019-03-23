# getpass_stream.py

import getpass
import sys


p = getpass.getpass(stream=sys.stderr)
print('Hai digitato:', p)
