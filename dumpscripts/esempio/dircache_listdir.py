import dircache

path = '.'
first = dircache.listdir(path)
second = dircache.listdir(path)

print 'Contents :', first
print 'Identical:', first is second
print 'Equal    :', first == second
