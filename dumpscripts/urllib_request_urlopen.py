# urllib_request_urlopen.py
from urllib import request

response = request.urlopen('http://localhost:8080/')
print('RISPOSTA     :', response)
print('URL          :', response.geturl())

headers = response.info()
print('DATA         :', headers['date'])
print('INTESTAZIONI :')
print('--------------')
print(headers)

data = response.read().decode('utf-8')
print('LUNGHEZZA     :', len(data))
print('DATI          :')
print('---------------')
print(data)
