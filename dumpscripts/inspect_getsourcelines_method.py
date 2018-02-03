# inspect_getsourcelines_method.py

import inspect
import pprint
import example

pprint.pprint(inspect.getsourcelines(example.A.get_name))
