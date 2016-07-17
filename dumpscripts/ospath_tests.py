import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './link_non_valido']:
    print "File               :", file
    print "Assoluto           :", os.path.isabs(file)
    print "E' un file?        :", os.path.isfile(file)
    print "E' una directory?  :", os.path.isdir(file)
    print "E' un  Link?       :", os.path.islink(file)
    print "Punto di montaggio?:", os.path.ismount(file)
    print 'Esiste?            :', os.path.exists(file)
    print 'Esiste il Link?    :', os.path.lexists(file)
    print
