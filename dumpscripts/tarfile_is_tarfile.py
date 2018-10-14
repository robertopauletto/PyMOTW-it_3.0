# tarfile_is_tarfile.py

import tarfile

for filename in ['LEGGIMI.txt', 'esempio.tar',
                 'cattivo_esempio.tar', 'nonqui.tar']:
    try:
        print('{:>15}  {}'.format(filename, tarfile.is_tarfile(
            filename)))
    except IOError as err:
        print('{:>15}  {}'.format(filename, err))
