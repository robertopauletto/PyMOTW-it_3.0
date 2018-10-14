# tarfile_addfile_string.py

import io
import tarfile

text = "Questi sono i dati da scrivere nell'archivio."
data = text.encode('utf-8')

with tarfile.open('tarfile_aggiungifile_stringa.tar', mode='w') as out:
    info = tarfile.TarInfo('file_inventato.txt')
    info.size = len(data)
    out.addfile(info, io.BytesIO(data))

print('Contenuto:')
with tarfile.open('tarfile_aggiungifile_stringa.tar', mode='r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
        f = t.extractfile(member_info)
        print(f.read().decode('utf-8'))
