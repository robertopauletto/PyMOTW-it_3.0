# tempfile_NamedTemporaryFile_args.py

import tempfile

with tempfile.NamedTemporaryFile(suffix='_suffisso',
                                 prefix='prefisso_',
                                 dir='/tmp') as temp:
    print('temp:')
    print('  ', temp)
    print('temp.name:')
    print('  ', temp.name)
