# contextlib_exitstack_enter_context.py

import contextlib


@contextlib.contextmanager
def make_context(i):
    print('{} in entrata'.format(i))
    yield {}
    print('{} in uscita'.format(i))


def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)


variable_stack(2, 'all\'interno del contesto')
