# tempfile_SpooledTemporaryFile_explicit.py

import tempfile

with tempfile.SpooledTemporaryFile(max_size=1000,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('Questa riga viene ripetuta ad libitum.\n')
        print(temp._rolled, temp._file)
    print('scrittura del buffer')
    temp.rollover()
    print(temp._rolled, temp._file)
