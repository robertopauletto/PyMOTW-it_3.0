# resource_setrlimit_nofile.py

import resource


soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print('Limite soft inizia come  :', soft)

resource.setrlimit(resource.RLIMIT_NOFILE, (4, hard))

soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print('Limite soft modificato in:', soft)

random = open('/dev/random', 'r')
print('random ha fd =', random.fileno())
try:
    null = open('/dev/null', 'w')
except IOError as err:
    print(err)
else:
    print('null ha fd =', null.fileno())
