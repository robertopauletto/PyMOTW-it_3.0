# inspect_getmembers_class_methods_b.py

import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.B, inspect.isfunction))
