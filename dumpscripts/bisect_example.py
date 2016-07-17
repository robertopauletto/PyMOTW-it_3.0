# bisect_example.py

import bisect

# UNa serie casuale di numeri
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('Nuovi Posizione Contenuto')
print('----- --------- ---------')

l = []
for i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:5}     {:5}'.format(i, position), l)
