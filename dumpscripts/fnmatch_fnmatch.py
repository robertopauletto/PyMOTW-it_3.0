import fnmatch
import os

pattern = 'fnmatch_*.py'
print 'Modello :', pattern
print

files = os.listdir('.')
for name in files:
    print 'Nome file: %-25s %s' % (name, fnmatch.fnmatch(name, pattern))
