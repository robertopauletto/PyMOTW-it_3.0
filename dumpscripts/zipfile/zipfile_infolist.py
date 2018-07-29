# zipfile_infolist.py

import datetime
import zipfile


def print_info(archive_name):
    with zipfile.ZipFile(archive_name) as zf:
        for info in zf.infolist():
            print(info.filename)
            print('  Commento    :', info.comment)
            mod_date = datetime.datetime(*info.date_time)
            print('  Modificato  :', mod_date)
            if info.create_system == 0:
                system = 'Windows'
            elif info.create_system == 3:
                system = 'Unix'
            else:
                system = 'SCONOSCIUTO'
            print('  Sistema      :', system)
            print('  Versione ZIP :', info.create_version)
            print('  Compressi    :', info.compress_size, 'byte')
            print('  Non compressi:', info.file_size, 'byte')
            print()

if __name__ == '__main__':
    print_info('esempio.zip')
