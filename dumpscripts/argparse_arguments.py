# argparse_arguments.py

import argparse

parser = argparse.ArgumentParser(
    description='Esempio con parametri non opzionali',
)

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print(parser.parse_args())
