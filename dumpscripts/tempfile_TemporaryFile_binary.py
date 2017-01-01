# tempfile_TemporaryFile_binary.py

import os
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Qualche dato')

    temp.seek(0)
    print(temp.read())
