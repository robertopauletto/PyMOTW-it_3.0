# atexit_exception.py
import atexit


def exit_with_exception(message):
    raise RuntimeError(message)


atexit.register(exit_with_exception, 'Registrato per primo')
atexit.register(exit_with_exception, 'Registrato per secondo')
