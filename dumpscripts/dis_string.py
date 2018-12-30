# dis_string.py

import dis

code = """
my_dict = {'a': 1}
"""

print('Disassemblato:\n')
dis.dis(code)

print('\nDettagli codice:\n')
dis.show_code(code)
