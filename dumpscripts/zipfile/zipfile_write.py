# zipfile_write.py

from zipfile_infolist import print_info
import zipfile

print('creazione archivio')
with zipfile.ZipFile('write.zip', mode='w') as zf:
    print('aggiungo LEGGIMI.txt')
    zf.write('LEGGIMI.txt')

print()
print_info('write.zip')
