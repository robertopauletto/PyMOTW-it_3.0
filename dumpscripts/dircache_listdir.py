import dircache

path = '.'
first = dircache.listdir(path)
second = dircache.listdir(path)

print 'Contenuto :', first
print 'Identica  :', first is second
print 'Uguale    :', first == second
