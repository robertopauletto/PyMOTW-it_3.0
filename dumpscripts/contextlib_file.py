# contextlib_file.py

with open('/tmp/pymotw.txt', 'wt') as f:
    f.write('il contenuto va qui')
# file viene chiuso automaticamente
