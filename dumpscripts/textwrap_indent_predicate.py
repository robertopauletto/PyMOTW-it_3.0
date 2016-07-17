# textwrap_indent_predicate.py

import textwrap
from textwrap_example import sample_text


def should_indent(line):
    print('Indentato {!r}?'.format(line))
    return len(line.strip()) % 2 == 0


dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'PARI ',
                        predicate=should_indent)

print('\nBlocco marcato:\n')
print(final)
