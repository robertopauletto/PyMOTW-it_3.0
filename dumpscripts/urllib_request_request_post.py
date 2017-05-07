# urllib_request_request_post.py

from urllib import parse
from urllib import request

query_args = {'q': 'query string', 'foo': 'bar'}

r = request.Request(
    url='http://localhost:8080/',
    data=parse.urlencode(query_args).encode('utf-8'),
)
print('Metodo di richiesta :', r.get_method())
r.add_header(
    'User-agent',
    'PyMOTW (https://pymotw.com/)',
)

print()
print('DATI IN USCITA:')
print(r.data)

print()
print('RISPOSTA DEL SERVER:')
print(request.urlopen(r).read().decode('utf-8'))
