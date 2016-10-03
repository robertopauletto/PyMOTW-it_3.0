# fnmatch_translate.py

import fnmatch

pattern = 'fnmatch_*.py'
print('Modello :', pattern)
print('Regex   :', fnmatch.translate(pattern))
