# inspect_getmembers_class_methods.py

import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.A, inspect.isfunction))
