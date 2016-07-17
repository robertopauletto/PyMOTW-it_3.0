from shutil import *
import os
from StringIO import StringIO
import sys

class VerboseStringIO(StringIO):
    def read(self, n=-1):
        next = StringIO.read(self, n)
        print 'read(%d) =>' % n, next
        return next

lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Vestibulum aliquam mollis dolor. Donec vulputate nunc ut diam. 
Ut rutrum mi vel sem. Vestibulum ante ipsum.'''

print 'Predefinito:'
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output)

print

print 'Tutto in una volta:'
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output, -1)

print

print 'Blocchi di 20:'
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output, 20)
