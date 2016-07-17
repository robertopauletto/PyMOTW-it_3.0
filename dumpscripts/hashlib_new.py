import hashlib
import sys


try:
    hash_name = sys.argv[1]
except IndexError:
    print "Specificare il nome dell'hash come primo parametro."
else:
    try:
        data = sys.argv[2]
    except IndexError:    
        from hashlib_data import lorem as data
    
    h = hashlib.new(hash_name)
    h.update(data)
    print h.hexdigest()

