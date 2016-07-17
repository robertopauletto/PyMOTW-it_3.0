#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import imp

module_types = { imp.PY_SOURCE:   'sorgente',
                 imp.PY_COMPILED: 'compilato',
                 imp.C_EXTENSION: 'estensione',
                 imp.PY_RESOURCE: 'risorsa',
                 imp.PKG_DIRECTORY: 'pacchetto',
                 }

def main():
    fmt = '%10s %10s %10s'
    print fmt % ('Estensione', 'Modalità', 'Tipe')
    print '-' * 32
    for extension, mode, module_type in imp.get_suffixes():
        print fmt % (extension, mode, module_types[module_type])

if __name__ == '__main__':
    main()