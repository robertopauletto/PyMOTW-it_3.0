import codecs
import locale
import sys

text = u'pi: p'

# Configura locale dalle impostazione di ambiente dell'utente.
locale.setlocale(locale.LC_ALL, '')

# Inserisce stdout all'interno di un writer che conosce la codifica.
lang, encoding = locale.getdefaultlocale()
print 'Codifica locale    :', encoding
sys.stdout = codecs.getwriter(encoding)(sys.stdout)

print 'Con stdout incapsulato:', text