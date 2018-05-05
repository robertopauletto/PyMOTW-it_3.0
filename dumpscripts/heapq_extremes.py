# heapq_extremes.py

import heapq
from heapq_heapdata import data

print('tutti          :', data)
print('3 più grandi   :', heapq.nlargest(3, data))
print('da ordinamento :', list(reversed(sorted(data)[-3:])))
print('3 più piccoli  :', heapq.nsmallest(3, data))
print('da ordinamento :', sorted(data)[:3])
