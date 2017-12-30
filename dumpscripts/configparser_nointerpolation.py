# configparser_nointerpolation.py

from configparser import ConfigParser

parser = ConfigParser(interpolation=None)
parser.read('interpolazione.ini')

print('Senza interpolazione:', parser.get('bug_tracker', 'url'))
