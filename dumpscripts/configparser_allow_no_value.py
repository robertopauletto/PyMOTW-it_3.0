# configparser_allow_no_value.py

import configparser

# Richiede valori
try:
    parser = configparser.ConfigParser()
    parser.read('consenti_no_valori.ini')
except configparser.ParsingError as err:
    print('Non posso elaborare:', err)

# Consente nomi di opzioni a se stanti
print('\nRiprovo con allow_no_value=True')
parser = configparser.ConfigParser(allow_no_value=True)
parser.read('consenti_no_valori.ini')
for flag in ['abilita_caratteristica_attivata',
             'abilita_altra_caratteristica_attivata']:
    print('\n', flag)
    exists = parser.has_option('flags', flag)
    print('  has_option:', exists)
    if exists:
        print('         get:', parser.get('flags', flag))
