# argparse_short.py

import argparse

parser = argparse.ArgumentParser(description='Breve app di esempio')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args(['-a', '-bvalore', '-c', '3']))
