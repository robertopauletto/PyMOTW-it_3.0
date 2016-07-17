import os.path

for parts in [ ('uno', 'due', 'tre'),
                       ('/', 'uno', 'due', 'tre'),
                                      ('/uno', '/due', '/tre'),
                                                     ]:
        print parts, ':', os.path.join(*parts)

