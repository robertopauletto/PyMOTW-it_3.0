# argparse_parent_with_group.py

import argparse

parser = argparse.ArgumentParser(add_help=False)

group = parser.add_argument_group('autenticazione')

group.add_argument('--user', action="store")
group.add_argument('--password', action="store")
