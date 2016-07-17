import fnmatch
import os

pattern = 'fnmatch_*.py'
print 'Modello :', pattern

files = os.listdir('.')
print 'File    :', files

print 'Corrispondenze :', fnmatch.filter(files, pattern)
