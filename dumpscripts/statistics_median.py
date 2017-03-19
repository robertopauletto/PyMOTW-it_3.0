# statistics_median.py

from statistics import *

data = [1, 2, 2, 5, 10, 12]

print('mediana    : {:0.2f}'.format(median(data)))
print('alto       : {:0.2f}'.format(median_low(data)))
print('basso      : {:0.2f}'.format(median_high(data)))
