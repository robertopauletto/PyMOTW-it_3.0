# cgitb_local_vars.py

import cgitb
cgitb.enable(format='text')


def func2(a, divisor):
    return a / divisor


def func1(a, b):
    c = b - 5
    return func2(a, c)

func1(1, 5)
