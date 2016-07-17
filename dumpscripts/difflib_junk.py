# difflib_junk.py

# Questo esempio è un adattamento dal sorgente di difflib.py.

from difflib import SequenceMatcher


def show_results(s):
    i, j, k = s.find_longest_match(0, 5, 0, 9)
    print('  i = {}'.format(i))
    print('  j = {}'.format(j))
    print('  k = {}'.format(k))
    print('  A[i:i+k] = {!r}'.format(A[i:i + k]))
    print('  B[j:j+k] = {!r}'.format(B[j:j + k]))

A = " abcd"
B = "abcd abcd"

print('A = {!r}'.format(A))
print('B = {!r}'.format(B))

print('\nSenza rilevamento di caratteri da ignorare:')
show_results(SequenceMatcher(None, A, B))

print('\nTratta gli spazi come caratteri da ignorare:')
show_results(SequenceMatcher(lambda x: x == " ", A, B))
