# pathlib_ownership.py
import pathlib

p = pathlib.Path(__file__)

print('Il proprietario di {} è {}/{}'.format(p, p.owner(), p.group()))
