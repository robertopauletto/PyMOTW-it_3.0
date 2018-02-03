# inspect_getmembers_class.py

import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.A), width=65)
