# configparser_read_many.py

from configparser import ConfigParser
import glob

parser = ConfigParser()

candidates = ['non_esiste.ini', 'anche_questo_non_esiste.ini',
              'semplice.ini', 'multisezione.ini']

found = parser.read(candidates)

missing = set(candidates) - set(found)

print('File configurazione trovati:', sorted(found))
print('File mancanti              :', sorted(missing))
