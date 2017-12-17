# argparse_conflict_handler_resolve.py

import argparse

parser = argparse.ArgumentParser(conflict_handler='resolve')

parser.add_argument('-a', action="store")
parser.add_argument('-b', action="store", help='Solo opzione breve')
parser.add_argument('--long-b', '-b',
                    action="store",
                    help='Opzione breve e verbosa insieme')

print(parser.parse_args(['-h']))
