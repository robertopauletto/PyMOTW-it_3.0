# inspect_signature_bind_partial.py

import inspect
import example

sig = inspect.signature(example.module_level_function)

partial = sig.bind_partial(
    'questo è arg1',
)

print('Senza predefiniti:')
for name, value in partial.arguments.items():
    print('{} = {!r}'.format(name, value))

print('\nCon predefiniti:')
partial.apply_defaults()
for name, value in partial.arguments.items():
    print('{} = {!r}'.format(name, value))
