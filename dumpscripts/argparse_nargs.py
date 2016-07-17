import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--tre', nargs=3)
parser.add_argument('--opzionale', nargs='?')
parser.add_argument('--tutti', nargs='*', dest='all')
parser.add_argument('--uno-o-piu', nargs='+')


print parser.parse_args()