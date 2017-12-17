# argparse_prefix_chars.py

import argparse

parser = argparse.ArgumentParser(
    description='Modifica i caratteri del prefisso di opzione',
    prefix_chars='-+/',
)

parser.add_argument('-a', action="store_false",
                    default=None,
                    help='Disattiva A',
                    )
parser.add_argument('+a', action="store_true",
                    default=None,
                    help='Attiva A',
                    )
parser.add_argument('//noarg', '++noarg',
                    action="store_true",
                    default=False)

print(parser.parse_args())
