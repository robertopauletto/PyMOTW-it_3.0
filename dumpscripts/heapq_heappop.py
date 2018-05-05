# heapq_heappop.py

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print('casuale :', data)
heapq.heapify(data)
print('con heap:')
show_tree(data)
print()

for i in range(2):
    smallest = heapq.heappop(data)
    print('rimosso {:>3}:'.format(smallest))
    show_tree(data)
