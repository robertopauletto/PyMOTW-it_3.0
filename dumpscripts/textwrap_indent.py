# textwrap_indent.py

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecondo paragrafo dopo una riga vuota.'
final = textwrap.indent(wrapped, '> ')

print('Blocco marcato:\n')
print(final)
