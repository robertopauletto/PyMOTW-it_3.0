# zipfile_is_zipfile.py

import zipfile

for filename in [ 'LEGGIMI.txt', 'esempio.zip',
                  'cattivo_esempio.zip', 'nonqui.zip' ]:
    print('{:>20}  {}'.format(
        filename, zipfile.is_zipfile(filename)))
