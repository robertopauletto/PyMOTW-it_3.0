# argparse_FileType.py

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i',
                    metavar='file-in-entrata', type=argparse.FileType('rt'))
parser.add_argument('-o',
                    metavar='file-in-uscita', type=argparse.FileType('wt'))

try:
    results = parser.parse_args()
    print('File in entrata:', results.i)
    print('File in uscita:', results.o)
except IOError as msg:
    parser.error(str(msg))
