# shlex_errors.py
import shlex

text = """Questa riga è a posto.
Questa riga ha un "apice non chiuso.
Anche questa riga è a posto.
"""

print('ORIGINALE: {!r}'.format(text))
print()

lexer = shlex.shlex(text)

print('TOKEN:')
try:
    for token in lexer:
        print('{!r}'.format(token))
except ValueError as err:
    first_line_of_error = lexer.token.splitlines()[0]
    print('ERRORE: {} {}'.format(lexer.error_leader(), err))
    print('segue {!r}'.format(first_line_of_error))
