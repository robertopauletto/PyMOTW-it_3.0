# sys_displayhook.py

import sys


class ExpressionCounter:

    def __init__(self):
        self.count = 0
        self.previous_value = self

    def __call__(self, value):
        print()
        print('  Precedente:', self.previous_value)
        print('  Nuovo     :', value)
        print()
        if value != self.previous_value:
            self.count += 1
            sys.ps1 = '({:3d})> '.format(self.count)
        self.previous_value = value
        sys.__displayhook__(value)


print('installazione')
sys.displayhook = ExpressionCounter()
