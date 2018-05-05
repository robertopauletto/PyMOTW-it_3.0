# heapq_heapreplace.py

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heapq.heapify(data)
print('inizio:')
show_tree(data)

for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('sostituzione di  {:>2} con {:>2}:'.format(smallest, n))
    show_tree(data)
