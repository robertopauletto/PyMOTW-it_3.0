# configparser_remove.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('multisezione.ini')

print('Lettura valori:\n')
for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print('  {} = {!r}'.format(name, value))

parser.remove_option('bug_tracker', 'password')
parser.remove_section('wiki')

print('\nModifica valori:\n')
for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print('  {} = {!r}'.format(name, value))
