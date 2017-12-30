# configparser_value_types.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('tipi.ini')

print('Interi:')
for name in parser.options('interi'):
    string_value = parser.get('interi', name)
    value = parser.getint('interi', name)
    print('  {:<12} : {!r:<7} -> {}'.format(
        name, string_value, value))

print('\nVirgola Mobile:')
for name in parser.options('virgola_mobile'):
    string_value = parser.get('virgola_mobile', name)
    value = parser.getfloat('virgola_mobile', name)
    print('  {:<12} : {!r:<7} -> {:0.2f}'.format(
        name, string_value, value))

print('\nBooleani:')
for name in parser.options('booleani'):
    string_value = parser.get('booleani', name)
    value = parser.getboolean('booleani', name)
    print('  {:<12} : {!r:<7} -> {}'.format(
        name, string_value, value))
