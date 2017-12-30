# configparser_read.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('semplice.ini')

print(parser.get('bug_tracker', 'url'))
