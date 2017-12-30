# configparser_multiline.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('multiriga.ini')

print(parser.get('esempio', 'messaggio'))
