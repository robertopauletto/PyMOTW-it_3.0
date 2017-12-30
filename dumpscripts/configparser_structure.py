# configparser_structure.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('multisezione.ini')

for section_name in parser.sections():
    print('Sezione:', section_name)
    print('  Opzioni:', parser.options(section_name))
    for name, value in parser.items(section_name):
        print('  {} = {}'.format(name, value))
    print()
