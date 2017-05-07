# os_rename_replace.py

import glob
import os


with open('inizio_rinomina.txt', 'w') as f:
    f.write('parte come inizio_rinomina.txt')

print('Partenza:', glob.glob('*rinomina.txt'))

os.rename('inizio_rinomina.txt', 'fine_rinomina.txt')

print('Dopo rinomina:', glob.glob('*rinomina.txt'))

with open('fine_rinomina.txt', 'r') as f:
    print('Contenuti:', repr(f.read()))

with open('rinomina_nuovi_contenuti.txt', 'w') as f:
    f.write('termina con i contenuti di rinomina_nuovi_contenuti.txt')

os.replace('rinomina_nuovi_contenuti.txt', 'fine_rinomina.txt')

with open('fine_rinomina.txt', 'r') as f:
    print('Dopo la sostituzione:', repr(f.read()))

for name in glob.glob('*rinomina.txt'):
    os.unlink(name)
