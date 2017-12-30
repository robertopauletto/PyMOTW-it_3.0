# configparser_has_section.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('multisezione.ini')

for candidate in ['wiki', 'bug_tracker', 'dvcs']:
    print('{:<12}: {}'.format(
        candidate, parser.has_section(candidate)))
