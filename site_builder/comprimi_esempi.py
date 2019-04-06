#!/usr/bin/env python
# -*- coding: utf-8 -*-
# comprimi_esempi

import zipfile
import os.path
from os import unlink


__doc__ = """nuovo script"""
__version__ = "0.1"
__changelog__ = """

"""


def comprimi(folder, elenco, outfolder, outfile):
    """Crea un file compresso (zip) con i file in elenco
    
    :param folder: la directory dei file di esempio 
    :param elenco: i file da comprimere
    :param outfile: il nome del file .zip (senza estensione)
    :return: il nome completo del file compresso
    """
    not_found = list()
    zipname = os.path.join(outfolder, outfile + ".zip")
    if os.path.exists(zipname):
        unlink(zipname)
    with zipfile.ZipFile(zipname, mode='w') as zf:
        for filename in elenco:
            fn = os.path.join(folder, filename)
            if not os.path.exists(fn):
                not_found.append(fn)
                continue
            zf.write(fn, os.path.basename(filename))
    return zipname, not_found
