# pdb_function_arguments.py

#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#

import pdb

def recursive_function(n=5, output='da stampare'):
    if n > 0:
        recursive_function(n-1)
    else:
        pdb.set_trace()
        print(output)
    return

if __name__ == '__main__':
    recursive_function()
