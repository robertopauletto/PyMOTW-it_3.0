# functools_wraps.py

import functools


def show_details(name, f):
    "Mostra i dettagli di un oggetto chiamabile."
    print('{}:'.format(name))
    print('  oggetto:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__', repr(f.__doc__))
    print()


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='Predefiniti del decorato', b=1):
        print('  decorato:', (a, b))
        print('  ', end=' ')
        f(a, b=b)
        return
    return decorated


def myfunc(a, b=2):
    "myfunc() non è complicata"
    print('  myfunc:', (a, b))
    return


# La funzione grezza
show_details('myfunc', myfunc)
myfunc('unwrapped, predefinito b')
myfunc('unwrapped, passggio di b', 3)
print()

# Wrap explicito
wrapped_myfunc = simple_decorator(myfunc)
show_details('wrapped_myfunc', wrapped_myfunc)
wrapped_myfunc()
wrapped_myfunc('args per wrapped', 4)
print()


# Wrap con la sintassi del decoratore
@simple_decorator
def decorated_myfunc(a, b):
    myfunc(a, b)
    return

show_details('decorated_myfunc', decorated_myfunc)
decorated_myfunc()
decorated_myfunc('args per decorato', 4)
