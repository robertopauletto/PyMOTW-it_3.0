# difflib_seq.py

import difflib
from difflib_data import *

s1 = [1, 2, 3, 5, 6, 4]
s2 = [2, 3, 5, 4, 6, 1]

print('Dati iniziali:')
print('s1 =', s1)
print('s2 =', s2)
print('s1 == s2:', s1 == s2)
print()

matcher = difflib.SequenceMatcher(None, s1, s2)
for tag, i1, i2, j1, j2 in reversed(matcher.get_opcodes()):

    if tag == 'delete':
        print('Elimina {} dalle posizioni [{}:{}]'.format(
            s1[i1:i2], i1, i2))
        del s1[i1:i2]

    elif tag == 'equal':
        print('s1[{}:{}] e s2[{}:{}] sono uguali'.format(
            i1, i2, j1, j2))

    elif tag == 'insert':
        print('Inserisce {} da s2[{}:{}] in s1 a {}'.format(
            s2[j1:j2], j1, j2, i1))
        s1[i1:i2] = s2[j1:j2]

    elif tag == 'replace':
        print(('Sostituisce {} da s1[{}:{}] '
               'con {} da s2[{}:{}]').format(
                   s1[i1:i2], i1, i2, s2[j1:j2], j1, j2))
        s1[i1:i2] = s2[j1:j2]

    print('  s1 =', s1)

print('s1 == s2:', s1 == s2)
