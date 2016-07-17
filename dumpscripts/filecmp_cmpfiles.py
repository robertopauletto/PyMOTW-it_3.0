import filecmp
import os

# Determina gli elementi che esistono in entrambe le directory
d1_contents = set(os.listdir('esempio/dir1'))
d2_contents = set(os.listdir('esempio/dir2'))
common = list(d1_contents & d2_contents)
common_files = [ f 
                for f in common 
                if os.path.isfile(os.path.join('esempio/dir1', f))
                ]
print 'File comuni:', common_files

# Confronta le directory
match, mismatch, errors = filecmp.cmpfiles('esempio/dir1', 
                                           'esempio/dir2', 
                                           common_files)
print 'Corrispondenza:', match
print 'Discrepanza:', mismatch
print 'Errori:', errors
