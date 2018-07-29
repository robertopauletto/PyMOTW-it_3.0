# zipfile_write_compression.py

from zipfile_infolist import print_info
import zipfile
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except (ImportError, AttributeError):
    compression = zipfile.ZIP_STORED

modes = {
    zipfile.ZIP_DEFLATED: 'compresso',
    zipfile.ZIP_STORED: 'conservato',
}

print('creazione archivio')
with zipfile.ZipFile('write_compression.zip', mode='w') as zf:
    mode_name = modes[compression]
    print('aggiungo LEGGIMI.txt con modalità compressione', mode_name)
    zf.write('LEGGIMI.txt', compress_type=compression)

print()
print_info('write_compression.zip')
