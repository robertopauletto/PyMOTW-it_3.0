# argparse_fromfile_prefix_chars.py

import argparse
import shlex

parser = argparse.ArgumentParser(description='Breve app di esempio',
                                 fromfile_prefix_chars='@',
                                 )

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args(['@argparse_fromfile_prefix_chars.txt']))
