# functools_update_wrapper.py

import functools


def myfunc(a, b=2):
    "Docstring per myfunc()."
    print('  chiamata myfunc con:', (a, b))


def show_details(name, f):
    "Mostra i dettagli di un oggetto chiamabile."
    print('{}:'.format(name))
    print('  object:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__', repr(f.__doc__))
    print()


show_details('myfunc', myfunc)

p1 = functools.partial(myfunc, b=4)
show_details('wrapper grezzo', p1)

print('Wrapper in aggiornamento:')
print('  assignazione:', functools.WRAPPER_ASSIGNMENTS)
print('  aggiornamento:', functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, myfunc)
show_details('Wrapper aggiornato', p1)
