# os_environ_example.py
import os

print('Valore iniziale:', os.environ.get('TESTVAR', None))
print('Processo figlio:')
os.system('echo $TESTVAR')

os.environ['TESTVAR'] = 'QUESTO VALORE E\' STATO CAMBIATO'

print()
print('Valore modificato:', os.environ['TESTVAR'])
print('Processo figlio:')
os.system('echo $TESTVAR')

del os.environ['TESTVAR']

print()
print('Valore rimosso:', os.environ.get('TESTVAR', None))
print('Processo figlio:')
os.system('echo $TESTVAR')
