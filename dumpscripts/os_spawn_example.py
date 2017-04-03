# os_spawn_example.py
import os

os.spawnlp(os.P_WAIT, 'pwd', 'pwd', '-P')
