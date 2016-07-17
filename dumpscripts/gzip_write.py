
import gzip
import os

outfilename = 'esempio.txt.gz'
output = gzip.open(outfilename, 'wb')
try:
    output.write('Il contenuto del file di esempio va qui.\n')
finally:
    output.close()

print outfilename, 'contiene', os.stat(outfilename).st_size, 'byte di dati compressi'
os.system('file -b --mime %s' % outfilename)
