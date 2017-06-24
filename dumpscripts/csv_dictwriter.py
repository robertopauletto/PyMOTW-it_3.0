# csv_dictwriter.py

import csv
import sys

fieldnames = ('Titolo 1', 'Titolo 2', 'Titolo 3', 'Titolo 4')
headers = {
    n: n
    for n in fieldnames
}
unicode_chars = 'å∫ç'

with open(sys.argv[1], 'wt') as f:

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(3):
        writer.writerow({
            'Titolo 1': i + 1,
            'Titolo 2': chr(ord('a') + i),
            'Titolo 3': '08/{:02d}/07'.format(i + 1),
            'Titolo 4': unicode_chars[i],
        })

print(open(sys.argv[1], 'rt').read())
