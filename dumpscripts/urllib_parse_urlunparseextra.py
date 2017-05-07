# urllib_parse_urlunparseextra.py

from urllib.parse import urlparse, urlunparse

original = 'http://netloc/path;?#'
print('ORIGINALE :', original)
parsed = urlparse(original)
print('ASSEMBLATO:', type(parsed), parsed)
t = parsed[:]
print('TUPLA     :', type(t), t)
print('NUOVO     :', urlunparse(t))
