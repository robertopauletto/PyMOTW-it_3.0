import fnmatch
import os

pattern = 'FNMATCH_*.PY'
print 'Modello :', pattern
print

files = os.listdir('.')
for name in files:
    print 'Nome file: %-25s %s' % (name,  fnmatch.fnmatchcase(name, pattern))
