# pyclbr_readmodule_ex.py

import pyclbr
import os
from operator import itemgetter

example_data = pyclbr.readmodule_ex('pyclbr_example')

for name, data in sorted(example_data.items(),
                         key=lambda x: x[1].lineno):
    if isinstance(data, pyclbr.Function):
        print('Funczione: {0} [{1}]'.format(name, data.lineno))
