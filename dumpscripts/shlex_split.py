# shlex_split.py

import shlex

text = """Questo testo ha "parti tra apici" al suo interno."""
print('ORIGINALE: {!r}'.format(text))
print()

print('TOKEN:')
print(shlex.split(text))
