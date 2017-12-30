# configparser_custom_types.py

from configparser import ConfigParser
import datetime


def parse_iso_datetime(s):
    print('parse_iso_datetime({!r})'.format(s))
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f')


parser = ConfigParser(
    converters={
        'datetime': parse_iso_datetime,
    }
)
parser.read('tipi_personalizzati.ini')

string_value = parser['dataora']['data_scadenza']
value = parser.getdatetime('dataora', 'data_scadenza')
print('data_scadenza : {!r} -> {!r}'.format(string_value, value))
