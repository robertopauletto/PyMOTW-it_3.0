# tarfile_addfile.py

import tarfile

print('creazione archivio')
with tarfile.open('tarfile_aggiuntofile.tar', mode='w') as out:
    print('aggiunto LEGGIMI.txt come RINOMINATO.txt')
    info = out.gettarinfo('LEGGIMI.txt', arcname='RINOMINATO.txt')
    out.addfile(info)

print()
print('Contenuto:')
with tarfile.open('tarfile_aggiuntofile.tar', mode='r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
