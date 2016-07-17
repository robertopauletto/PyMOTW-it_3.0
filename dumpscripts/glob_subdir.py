import glob

print 'Sottodirectory nominata esplicitamente:'
for name in glob.glob('dir/subdir/*'):
    print '\t', name

print 'Sottodirectory nominata con caratteri jolly:'
for name in glob.glob('dir/*/*'):
    print '\t', name
