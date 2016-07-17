import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--modo', choices=('sola-lettura', 'lettura-scrittura'))

print parser.parse_args()