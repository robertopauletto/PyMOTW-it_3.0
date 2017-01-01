# tempfile_TemporaryDirectory.py

import pathlib
import tempfile

with tempfile.TemporaryDirectory() as directory_name:
    the_dir = pathlib.Path(directory_name)
    print(the_dir)
    a_file = the_dir / 'un_file.txt'
    a_file.write_text('Questo file viene eliminato.')

print('La directory eiste dopo?', the_dir.exists())
print('Contenuto dopo:', list(the_dir.glob('*')))
