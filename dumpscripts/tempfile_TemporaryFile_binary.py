import os
import tempfile

temp = tempfile.TemporaryFile()
try:
    temp.write('Qualche dato')
    temp.seek(0)
    
    print temp.read()
finally:
    temp.close()
