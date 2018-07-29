# zipfile_writestr_zipinfo.py

import time
import zipfile
from zipfile_infolist import print_info

msg = b'Questi dati non esistono in un file.'

with zipfile.ZipFile('writestr_zipinfo.zip',
                     mode='w',
                     ) as zf:
    info = zipfile.ZipInfo('da_stringa.txt',
                           date_time=time.localtime(time.time()),
                           )
    info.compress_type = zipfile.ZIP_DEFLATED
    info.comment = b'I commenti vanno qui'
    info.create_system = 0
    zf.writestr(info, msg)

print_info('writestr_zipinfo.zip')

