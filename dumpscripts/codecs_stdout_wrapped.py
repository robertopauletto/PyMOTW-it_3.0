import codecs
import sys

text = u'pi: p'

# Si inserisce sys.stdout in un writer che sa come
#gestire la codifica
# Dati Unicode.
wrapped_stdout = codecs.getwriter('UTF-8')(sys.stdout)
wrapped_stdout.write(u'Tramite write: ' + text + '\n')

# Sostituzione di sys.stdout con un writer
sys.stdout = wrapped_stdout

print u'Tramite print:', text