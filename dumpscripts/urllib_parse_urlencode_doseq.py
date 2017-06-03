# urllib_parse_urlencode_doseq.py

from urllib.parse import urlencode

query_args = {
    'foo': ['foo1', 'foo2'],
}
print('Singola :', urlencode(query_args))
print('Sequenza:', urlencode(query_args, doseq=True))
