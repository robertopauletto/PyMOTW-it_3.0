# tarfile_extractall.py

import tarfile
import os

os.mkdir('outdir')
with tarfile.open('esempio.tar', 'r') as t:
    t.extractall('outdir')
print(os.listdir('outdir'))
