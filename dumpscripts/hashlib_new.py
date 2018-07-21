# hashlib_new.py

import argparse
import hashlib
import sys

from hashlib_data import lorem


parser = argparse.ArgumentParser('demo hashlib')
parser.add_argument(
    'hash_name',
    choices=hashlib.algorithms_available,
    help="il nome dell'algoritmo da usare per l'hash",
)
parser.add_argument(
    'data',
    nargs='?',
    default=lorem,
    help="i dati in input per l'hash, predefinito lorem ipsum",
)
args = parser.parse_args()

h = hashlib.new(args.hash_name)
h.update(args.data.encode('utf-8'))
print(h.hexdigest())
