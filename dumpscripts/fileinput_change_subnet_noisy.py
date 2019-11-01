# fileinput_change_subnet_noisy.py

import fileinput
import glob
import sys

from_base = sys.argv[1]
to_base = sys.argv[2]
files = sys.argv[3:]

for line in fileinput.input(files, inplace=True):
    if fileinput.isfirstline():
        sys.stderr.write('Iniziata elaborazione {}\n'.format(
            fileinput.filename()))
        sys.stderr.write('La directory contiene: {}\n'.format(
            glob.glob('etc_hosts.txt*')))
    line = line.rstrip().replace(from_base, to_base)
    print(line)

sys.stderr.write('Terminata elaborazione\n')
sys.stderr.write('La directory contiene: {}\n'.format(
    glob.glob('etc_hosts.txt*')))
