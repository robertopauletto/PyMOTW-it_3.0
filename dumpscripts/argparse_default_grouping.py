# argparse_default_grouping.py

import argparse

parser = argparse.ArgumentParser(description='Piccola semplice app')

parser.add_argument('--opzionale', action="store_true",
                    default=False)
parser.add_argument('posizionale', action="store")

print(parser.parse_args())
