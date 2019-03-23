# dis_test_loop.py

import dis
import sys
import textwrap
import timeit


module_name = sys.argv[1]
module = __import__(module_name)
Dictionary = module.Dictionary

dis.dis(Dictionary.load_data)
print()
t = timeit.Timer(
    'd = Dictionary(words)',
    textwrap.dedent("""
    from {module_name} import Dictionary
    words = [
        l.strip()
        for l in open('/usr/share/dict/mywords', 'rt')
    ]
    """).format(module_name=module_name)
    )
iterations = 10
print('TEMPO: {:0.4f}'.format(t.timeit(iterations) / iterations))
