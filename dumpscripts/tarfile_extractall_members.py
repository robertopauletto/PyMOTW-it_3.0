# tarfile_extractall_members.py

import tarfile
import os

os.mkdir('outdir')
with tarfile.open('esempio.tar', 'r') as t:
    t.extractall('outdir',
                 members=[t.getmember('LEGGIMI.txt')],
                 )
print(os.listdir('outdir'))

