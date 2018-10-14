# tarfile_extract.py

import tarfile
import os

os.mkdir('outdir')
with tarfile.open('esempio.tar', 'r') as t:
    t.extract('LEGGIMI.txt.txt', 'outdir')
print(os.listdir('outdir'))
