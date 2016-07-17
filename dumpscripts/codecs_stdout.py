import codecs
import sys

text = u'pi: p'

# La stampa verso stdout potrebbe causare un errore di codifica
print 'encoding predefinito:', sys.stdout.encoding
print 'TTY:', sys.stdout.isatty()
print text