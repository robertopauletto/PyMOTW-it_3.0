# configparser_structure_dict.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('multisezione.ini')

for section_name in parser:
    print('Sezione:', section_name)
    section = parser[section_name]
    print('  Opzioni:', list(section.keys()))
    for name in section:
        print('  {} = {}'.format(name, section[name]))
    print()
