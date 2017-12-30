# configparser_extendedinterpolation.py

from configparser import ConfigParser, ExtendedInterpolation

parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.read('interpolazione_estesa.ini')

print('Valore originale     :', parser.get('bug_tracker', 'url'))

parser.set('intranet', 'port', '9090')
print('Valore porta alterato:', parser.get('bug_tracker', 'url'))

print('Senza interpolazione :', parser.get('bug_tracker', 'url',
                                           raw=True))
