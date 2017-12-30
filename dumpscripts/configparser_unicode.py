# configparser_unicode.py

from configparser import ConfigParser

parser = ConfigParser()
# Apertura del file con la codifica corretta
parser.read('unicode.ini', encoding='utf-8')

password = parser.get('bug_tracker', 'password')

print('Password:', password.encode('utf-8'))
print('Tipe    :', type(password))
print('repr()  :', repr(password))
