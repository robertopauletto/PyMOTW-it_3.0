# tarfile_add.py

import tarfile

print('creazione archivio')
with tarfile.open('tarfile_aggiunto.tar', mode='w') as out:
    print('aggiunto LEGGIMI.txt')
    out.add('LEGGIMI.txt')

print()
print('Contenuto:')
with tarfile.open('tarfile_aggiunto.tar', mode='r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
