# pathlib_touch.py

import pathlib
import time

p = pathlib.Path('toccato')
if p.exists():
    print('esiste già')
else:
    print('creato nuovo')

p.touch()
start = p.stat()

time.sleep(1)

p.touch()
end = p.stat()

print('Inizio:', time.ctime(start.st_mtime))
print('Fine  :', time.ctime(end.st_mtime))
