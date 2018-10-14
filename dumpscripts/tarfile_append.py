# tarfile_append.py

import tarfile

print('creazione archivio')
with tarfile.open('tarfile_accoda.tar', mode='w') as out:
    out.add('LEGGIMI.txt')

print('contenuto:',)
with tarfile.open('tarfile_accoda.tar', mode='r') as t:
    print([m.name for m in t.getmembers()])

print('si accoda index.rst')
with tarfile.open('tarfile_accoda.tar', mode='a') as out:
    out.add('index.rst')

print('contenuto:',)
with tarfile.open('tarfile_accoda.tar', mode='r') as t:
    print([m.name for m in t.getmembers()])
