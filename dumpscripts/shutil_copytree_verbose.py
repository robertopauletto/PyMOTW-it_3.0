# shutil_copytree_verbose.py

import glob
import pprint
import shutil


def verbose_copy(src, dst):
    print('in copia\n {!r}\n verso {!r}'.format(src, dst))
    return shutil.copy2(src, dst)


print('PRIMA:')
pprint.pprint(glob.glob('/tmp/example/*'))
print()

shutil.copytree(
    '../shutil', '/tmp/example',
    copy_function=verbose_copy,
    ignore=shutil.ignore_patterns('*.py'),
)

print('\nDOPO:')
pprint.pprint(glob.glob('/tmp/example/*'))
