# string_template.py
import string

values = {'var': 'foo'}

t = string.Template("""
Variabile         : $var
Escape            : $$
Variabile in testo: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variabile         : %(var)s
Escape            : %%
Variabile in testo: %(var)siable
"""

print('INTERPOLAZIONE:', s % values)

s = """
Variabile         : {var}
Escape            :  {{}}
Variabile in testo: {var}iable
"""

print('FORMAT:', s.format(**values))
