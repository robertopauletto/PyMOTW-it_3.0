# dis_traceback.py

#!/usr/bin/env python
# encoding: utf-8

i = 1
j = 0
k = 3


try:
    result = k * (i / j) + (i / k)
except Exception:
    import dis
    import sys
    exc_type, exc_value, exc_tb = sys.exc_info()
    dis.distb(exc_tb)
