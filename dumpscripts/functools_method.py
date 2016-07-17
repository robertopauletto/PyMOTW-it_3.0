#functools_method.py

import functools


class MyClass:
    "Classe Demo per functools"

    def method1(self, a, b=2):
        "Docstring per method1()."
        print('  chiamato method1 con:', (self, a, b))

    def method2(self, c, d=5):
        "Docstring per method2"
        print('  chiamato method2 con:', (self, c, d))

    wrapped_method2 = functools.partial(method2, 'wrapped c')
    functools.update_wrapper(wrapped_method2, method2)

    def __call__(self, e, f=6):
        "Docstring per MyClass.__call__"
        print('  chiamato object con:', (self, e, f))


def show_details(name, f):
    "Mostra dettagli di un oggetto chiamabile"
    print('{}:'.format(name))
    print('  oggetto:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__', repr(f.__doc__))
    return


o = MyClass()

show_details('chiamata di method1 direttamente', o.method1)
o.method1('nessun predefinito per a', b=3)
print()

p1 = functools.partial(o.method1, b=4)
functools.update_wrapper(p1, o.method1)
show_details('chiamata di method1 wrapped', p1)
p1('a va qui')
print()

show_details('chiamata di method2 direttamente', o.method2)
o.method2('nessun predefinito per  c', d=6)
print()

show_details('chiamata di method2 wrapped', o.wrapped_method2)
o.wrapped_method2('nessun predefinito per  c', d=7)
print()

show_details('instanza', o)
o('nessun predefinito per  e')
print()

p2 = functools.partial(o, f=8)
functools.update_wrapper(p2, o)
show_details('wrapper di istanza', p2)
p2('e va qui')
