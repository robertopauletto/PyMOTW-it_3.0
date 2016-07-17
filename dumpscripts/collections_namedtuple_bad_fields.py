# collections_namedtuple_bad_fields.py

import collections

try:
    collections.namedtuple('Persona', 'name class anni')
except ValueError as err:
    print(err)

try:
    collections.namedtuple('Persona', 'nome anni anni')
except ValueError as err:
    print(err)
