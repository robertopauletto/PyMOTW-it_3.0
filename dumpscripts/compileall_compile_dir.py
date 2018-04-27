#compileall_compile_dir.py

import compileall
import glob


def show(title):
    print(title)
    for filename in glob.glob('esempi/**',
                              recursive=True):
        print('  {}'.format(filename))
    print()


show('Prima')

compileall.compile_dir('esempi')

show('\nDopo')
