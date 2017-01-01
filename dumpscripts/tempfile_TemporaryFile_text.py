# tempfile_TemporaryFile_text.py

import tempfile

with tempfile.TemporaryFile(mode='w+t') as f:
    f.writelines(['primo\n', 'secondo\n'])

    f.seek(0)
    for line in f:
        print(line.rstrip())
