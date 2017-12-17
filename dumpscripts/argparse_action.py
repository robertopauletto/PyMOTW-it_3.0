# argparse_action.py

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store',
                    dest='simple_value',
                    help='Conserva un valore semplice')

parser.add_argument('-c', action='store_const',
                    dest='constant_value',
                    const='value-to-store',
                    help='Conserva un valore costante')

parser.add_argument('-t', action='store_true',
                    default=False,
                    dest='boolean_t',
                    help='Imposta un interruttore a True')
parser.add_argument('-f', action='store_false',
                    default=True,
                    dest='boolean_f',
                    help='Imposta un interruttore a False')

parser.add_argument('-a', action='append',
                    dest='collection',
                    default=[],
                    help='Aggiunge velori ripetuti in una lista')

parser.add_argument('-A', action='append_const',
                    dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Aggiunge valori diversi ad una lista')
parser.add_argument('-B', action='append_const',
                    dest='const_collection',
                    const='value-2-to-append',
                    help='Aggiunge valori diversi ad una lista')

parser.add_argument('--versione', action='version',
                    version='%(prog)s 1.0')

results = parser.parse_args()
print('valore_semplice  = {!r}'.format(results.simple_value))
print('valore_costante  = {!r}'.format(results.constant_value))
print('booleano_true    = {!r}'.format(results.boolean_t))
print('booleano_false   = {!r}'.format(results.boolean_f))
print('collezione       = {!r}'.format(results.collection))
print('collezione_cost. = {!r}'.format(results.const_collection))
