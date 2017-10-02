# pathlib_types.py

import itertools
import os
import pathlib

root = pathlib.Path('file_di_prova')

# Pulisce quanto elaborato nelle precedenti esecuzioni
if root.exists():
    for f in root.iterdir():
        f.unlink()
else:
    root.mkdir()

# Crea i file di prova
(root / 'file').write_text(
    'Questo è un file normale', encoding='utf-8')
(root / 'symlink').symlink_to('file')
os.mkfifo(str(root / 'fifo'))

# Verifica il tipo di file
to_scan = itertools.chain(
    root.iterdir(),
    [pathlib.Path('/dev/disk0'),
     pathlib.Path('/dev/console')],
)
hfmt = '{:18s}' + ('  {:>5}' * 6)
print(hfmt.format('Nome', 'File', 'Dir', 'Link', 'FIFO', 'Blocco',
                  'Carattere'))
print()

fmt = '{:20s}  ' + ('{!r:>5}  ' * 6)
for f in to_scan:
    print(fmt.format(
        str(f),
        f.is_file(),
        f.is_dir(),
        f.is_symlink(),
        f.is_fifo(),
        f.is_block_device(),
        f.is_char_device(),
    ))
