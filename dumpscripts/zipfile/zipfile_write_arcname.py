# zipfile_write_arcname.py

from zipfile_infolist import print_info
import zipfile

with zipfile.ZipFile('write_arcname.zip', mode='w') as zf:
    zf.write('LEGGIMI.txt', arcname='NON_LEGGIMI.txt')

print_info('write_arcname.zip')
