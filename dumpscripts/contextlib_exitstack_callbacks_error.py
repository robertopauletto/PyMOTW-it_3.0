# contextlib_exitstack_callbacks_error.py

import contextlib


def callback(*args, **kwds):
    print('callback di chiusura({}, {})'.format(args, kwds))


try:
    with contextlib.ExitStack() as stack:
        stack.callback(callback, 'arg1', 'arg2')
        stack.callback(callback, arg3='val3')
        raise RuntimeError('errore sollevato')
except RuntimeError as err:
    print('ERRORE: {}'.format(err))
