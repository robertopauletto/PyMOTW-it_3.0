# os_walk.py

import os
import sys

# Se non viene passato un percorso da elencare, si usa /tmp
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print(dir_name)
    # Risalta i nomi delle sotto-directory aggiungendo una /
    sub_dirs = [n + '/' for n in sub_dirs]
    # Combina i contenuti delle directory assieme
    contents = sub_dirs + files
    contents.sort()
    # Mostra il contenuto
    for c in contents:
        print('  {}'.format(c))
    print()
