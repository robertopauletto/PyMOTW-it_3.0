# compileall_exclude_dirs.py

import compileall
import re

compileall.compile_dir(
    'esempi',
    rx=re.compile(r'/subdir'),
)
