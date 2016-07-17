from shutil import *
from glob import glob

f = open('esempio.txt', 'wt')
f.write('contenuto')
f.close()

print 'PRIMA: ', glob('esempio*')
move('esempio.txt', 'esempio.out')
print 'DOPO : ', glob('esempio*')
