# os_cwd_example.py
import os

print('Partenza:', os.getcwd())

print('Risalita di un livello:', os.pardir)
os.chdir(os.pardir)

print('Dopo lo spostamento:', os.getcwd())
