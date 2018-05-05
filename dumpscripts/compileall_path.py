# compileall_path.py

import compileall
import sys

sys.path[:] = ['esempi', 'nonqui']
print('sys.path =', sys.path)
compileall.compile_path()
