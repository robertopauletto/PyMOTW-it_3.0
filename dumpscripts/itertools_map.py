# itertools_map.py


def times_two(x):
    return 2 * x


def multiply(x, y):
    return (x, y, x * y)


print('Doppi:')
for i in map(times_two, range(5)):
    print(i)

print('\nMultipli:')
r1 = range(5)
r2 = range(5, 10)
for i in map(multiply, r1, r2):
    print('{:d} * {:d} = {:d}'.format(*i))

print('\nFine:')
r1 = range(5)
r2 = range(2)
for i in map(multiply, r1, r2):
    print(i)
