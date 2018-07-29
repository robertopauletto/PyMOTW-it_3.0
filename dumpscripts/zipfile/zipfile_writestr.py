# zipfile_writestr.py

from zipfile_infolist import print_info
import zipfile

msg = 'Questi dati non esistono in un file.'
with zipfile.ZipFile('writestr.zip',
                     mode='w',
                     compression=zipfile.ZIP_DEFLATED,
                     ) as zf:
    zf.writestr('da_una_stringa.txt', msg)

print_info('writestr.zip')

with zipfile.ZipFile('writestr.zip', 'r') as zf:
    print(zf.read('da_una_stringa.txt'))
