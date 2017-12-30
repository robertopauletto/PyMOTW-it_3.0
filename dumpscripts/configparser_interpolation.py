# configparser_interpolation.py

from configparser import ConfigParser

parser = ConfigParser()
parser.read('interpolazione.ini')

print('Valore originale       :', parser.get('bug_tracker', 'url'))

parser.set('bug_tracker', 'port', '9090')
print('Valore porta modificato:', parser.get('bug_tracker', 'url'))

print('Senza interpolazione   :', parser.get('bug_tracker', 'url',
                                           raw=True))
