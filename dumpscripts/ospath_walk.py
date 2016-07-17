import os
import os.path
import pprint

def visit(arg, dirname, names):
    print dirname, arg
    for name in names:
        subname = os.path.join(dirname, name)
        if os.path.isdir(subname):
            print '  %s/' % name
        else:
            print '  %s' % name
    print

os.mkdir('esempio')
os.mkdir('esempio/uno')
f = open('esempio/uno/file.txt', 'wt')
f.write('contenuto')
f.close()
f = open('esempio/due.txt', 'wt')
f.write('contenuto')
f.close()
os.path.walk('esempio', visit, '(Dati utente)')
