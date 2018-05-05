# compileall_recursion_depth.py

import compileall
import re

compileall.compile_dir(
    'esempi',
    maxlevels=0,
)
