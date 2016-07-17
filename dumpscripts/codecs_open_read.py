import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print 'Lettura da: ', filename
with codecs.open(filename, mode='rt', encoding=encoding) as f:
    print repr(f.read())