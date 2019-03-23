# distmp.py

from string import ascii_letters

l = [word.strip() for word in open('/usr/share/dict/words')
     if word[0] in ascii_letters]

open('mywords', mode='w').write('\n'.join(l))
