# functools_partial.py

import functools


def myfunc(a, b=2):
    "Docstring per myfunc()."
    print('  chiamata myfunc con:', (a, b))


def show_details(name, f, is_partial=False):
    "Mostra i dettagli di un oggetto chiamabile."
    print('{}:'.format(name))
    print('  oggetto:', f)
    if not is_partial:
        print('  __name__:', f.__name__)
    if is_partial:
        print('  func:', f.func)
        print('  args:', f.args)
        print('  keywords:', f.keywords)
    return


show_details('myfunc', myfunc)
myfunc('a', 3)
print()

# Imposta un valore predefinito diverso per 'b' ma chiede al
# chiamante di fornire 'a'.
p1 = functools.partial(myfunc, b=4)
show_details('partial con predefiniti determinati', p1, True)
p1('passato a')
p1('override di b', b=5)
print()

# Imposta valori predefiniti sia per 'a' che per 'b'.
p2 = functools.partial(myfunc, 'predefinito a', b=99)
show_details('partial con predefiniti', p2, True)
p2()
p2(b='override di b')
print()

print('Argomenti insufficienti:')
p1()
