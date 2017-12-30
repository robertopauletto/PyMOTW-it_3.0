# configparser_has_option.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('multisezione.ini')

SECTIONS = ['wiki', 'none']
OPTIONS = ['username', 'password', 'url', 'descrizione']

for section in SECTIONS:
    has_section = parser.has_section(section)
    print('{} sezione esiste: {}'.format(section, has_section))
    for candidate in OPTIONS:
        has_option = parser.has_option(section, candidate)
        print('{}.{:<12}  : {}'.format(
            section, candidate, has_option))
    print()
