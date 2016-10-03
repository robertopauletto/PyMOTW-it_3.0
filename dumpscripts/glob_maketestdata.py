# glob_maketestdata.py

import os
import os.path
import glob

if not os.path.exists('dir'):
    os.mkdir('dir')
if not os.path.exists('dir/subdir'):
    os.mkdir('dir/subdir')
os.chdir('dir')
fh = open('file.txt', 'w')
fh.close()
fh = open('file1.txt', 'w')
fh.close()
fh = open('file2.txt', 'w')
fh.close()
fh = open('filea.txt', 'w')
fh.close()
fh = open('fileb.txt', 'w')
fh.close()
fh = open('file?.txt', 'w')
fh.close()
fh = open('file*.txt', 'w')
fh.close()
fh = open('file[.txt', 'w')
fh.close()
fh = open('subdir/subfile.txt', 'w')
fh.close()
print("\n".join(glob.glob('dir')))
print("\n".join(sorted(glob.glob('dir/*'))))
print("\n".join(sorted(glob.glob('dir/subdir/*'))))
