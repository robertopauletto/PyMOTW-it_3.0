import codecs
import locale
import sys

# Configura locale dalle impostazioni di ambiente dell'utente
locale.setlocale(locale.LC_ALL, '')

# Inserisce stdin in un lettore in grado di eseguire una codifica
lang, encoding = locale.getdefaultlocale()
sys.stdin = codecs.getreader(encoding)(sys.stdin)

print 'Da stdin:', repr(sys.stdin.read())