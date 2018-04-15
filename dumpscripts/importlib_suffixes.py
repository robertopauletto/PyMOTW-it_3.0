# importlib_suffixes.py

import importlib.machinery

SUFFIXES = [
    ('Sorgente:', importlib.machinery.SOURCE_SUFFIXES),
    ('Debug:',
     importlib.machinery.DEBUG_BYTECODE_SUFFIXES),
    ('Ottimizzato:',
     importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES),
    ('Bytecode:', importlib.machinery.BYTECODE_SUFFIXES),
    ('Estensione:', importlib.machinery.EXTENSION_SUFFIXES),
]


def main():
    tmpl = '{:<12}  {}'
    for name, value in SUFFIXES:
        print(tmpl.format(name, value))


if __name__ == '__main__':
    main()
