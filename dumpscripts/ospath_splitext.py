import os.path

for path in [ 'nomefile.txt', 'nomefile', '/percorso/al/nomefile.txt', '/', '' ]:
        print '"%s" :' % path, os.path.splitext(path)
            
