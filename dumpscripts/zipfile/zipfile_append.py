# zipfile_append.py

from zipfile_infolist import print_info
import zipfile

print('creazione archivio')
with zipfile.ZipFile('append.zip', mode='w') as zf:
    zf.write('LEGGIMI.txt')

print()
print_info('append.zip')

print("aggiungo all'archivio")
with zipfile.ZipFile('append.zip', mode='a') as zf:
    zf.write('LEGGIMI.txt', arcname='LEGGIMI2.txt')

print()
print_info('append.zip')
