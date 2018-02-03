# inspect_signature_bind.py

import inspect
import example

sig = inspect.signature(example.module_level_function)

bound = sig.bind(
    'questo è arg1',
    'questo è arg2',
    'questo è un argomento supplementare posizionale',
    extra_named_arg='value',
)

print('Argomenti:')
for name, value in bound.arguments.items():
    print('{} = {!r}'.format(name, value))

print('\nChiamata:')
print(example.module_level_function(*bound.args, **bound.kwargs))
