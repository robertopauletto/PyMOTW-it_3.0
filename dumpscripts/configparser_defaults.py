# configparser_defaults.py

import configparser

# Definisce i nomi delle opzioni
option_names = [
    'from-default',
    'from-section', 'section-only',
    'file-only', 'init-only', 'init-and-file',
    'from-vars',
]

# Inizializza il parser con qualche valore di default
DEFAULTS = {
    'from-default': 'valore da DEFAULTS passato ad init',
    'init-only': 'valore da DEFAULTS passato ad init',
    'init-and-file': 'valore da DEFAULTS passato ad init',
    'from-section': 'valore da DEFAULTS passato ad init',
    'from-vars': 'valore da DEFAULTS passato ad init',
}
parser = configparser.ConfigParser(defaults=DEFAULTS)

print('Default prima di caricare il file:')
defaults = parser.defaults()
for name in option_names:
    if name in defaults:
        print('  {:<15} = {!r}'.format(name, defaults[name]))

# Carica il file di configurazione
parser.read('with-defaults.ini')

print('\nDefault dopo il caricamento del file:')
defaults = parser.defaults()
for name in option_names:
    if name in defaults:
        print('  {:<15} = {!r}'.format(name, defaults[name]))

# Definisce alcuni valori locali da sovrascriver
vars = {'from-vars': 'valori da vars'}

# Mostra i valori di tutte le opzioni
print('\nRicerca opzioni:')
for name in option_names:
    value = parser.get('sect', name, vars=vars)
    print('  {:<15} = {!r}'.format(name, value))

# Mostra messaggi di errore per opzioni che non esistono
print('\nCasi di errore:')
try:
    print('Opzione non esiste :', parser.get('sect', 'no-option'))
except configparser.NoOptionError as err:
    print(err)

try:
    print('Sezione non esiste:', parser.get('no-sect', 'no-option'))
except configparser.NoSectionError as err:
    print(err)
