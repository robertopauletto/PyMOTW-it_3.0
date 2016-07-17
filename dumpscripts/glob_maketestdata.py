import os


if not os.path.exists('dir'): os.mkdir('dir')
if not os.path.exists('dir/subdir'): os.mkdir('dir/subdir')
os.chdir('dir')
fh = file ('file.txt', 'w')
fh.close();
fh = file ('file1.txt', 'w')
fh.close();
fh = file ('file2.txt', 'w')
fh.close();
fh = file ('filea.txt', 'w')
fh.close();
fh = file ('fileb.txt', 'w')
fh.close();
fh = file ('subdir/subfile.txt', 'w')
fh.close();

