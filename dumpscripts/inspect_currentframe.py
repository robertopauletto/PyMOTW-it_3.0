# inspect_currentframe.py

import inspect
import pprint


def recurse(limit, keyword='predefinito', *, kwonly='deve essere nominativo'):
    local_variable = '.' * limit
    keyword = 'modificato valore dell\'argomento'
    frame = inspect.currentframe()
    print('riga {} di {}'.format(frame.f_lineno,
                                 frame.f_code.co_filename))
    print('locali:')
    pprint.pprint(frame.f_locals)
    print()
    if limit <= 0:
        return
    recurse(limit - 1)
    return local_variable

if __name__ == '__main__':
    recurse(2)
