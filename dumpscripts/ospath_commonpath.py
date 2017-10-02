# ospath_commonpath.py
import os.path

paths = ['/uno/due/tre/quattro',
         '/uno/due/trequalchealtro',
         '/uno/due/tre/'
         ]
for path in paths:
    print('PERCORSO:', path)

print()
print('PREFISSO:', os.path.commonpath(paths))
