import os.path

for path in [ 'uno//due//tre', 
                      'uno/./due/./tre', 
                                    'uno/../uno/due/tre',
                                                  ]:
        print path, ':', os.path.normpath(path)
