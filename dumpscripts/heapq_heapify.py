# heapq_heapify.py

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print('casuali :', data)
heapq.heapify(data)
print('con heap:')
show_tree(data)
