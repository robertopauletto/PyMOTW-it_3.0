# configparser_interpolation_defaults.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('interpolazione_predefiniti.ini')

print('URL:', parser.get('bug_tracker', 'url'))
