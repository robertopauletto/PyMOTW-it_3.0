# argparse_with_shlex.py

import argparse
from configparser import ConfigParser
import shlex

parser = argparse.ArgumentParser(description='Breve app di esempio')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

config = ConfigParser()
config.read('argparse_with_shlex.ini')
config_value = config.get('cli', 'options')
print('Da configurazione :', config_value)

argument_list = shlex.split(config_value)
print('Da lista argomenti:', argument_list)

print('Risulati          :', parser.parse_args(argument_list))

