import linecache

# Gli errori sono nascosti anche se linecache non trova il file
no_such_file = linecache.getline('this_file_does_not_exist.txt', 1)
print '\nNESSUN FILE: ', no_such_file
