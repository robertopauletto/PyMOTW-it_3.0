#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""
Versione %s %s
""" % ( __version__, __date__ )

import datetime
import codecs
import sys
import os.path
import os
from stat import * 
from shutil import copy
import re
from collections import defaultdict
sys.path.append(r'../lib')
sys.path.append(r'../database')

from common import get_root

OLD_HTML_FOLDER = r'Dropbox/Code/python/pymotw-it/html'
OLD_TRAN_FOLDER = r'Dropbox/Code/python/pymotw-it/tran'

def html_path():
    """
    Metodo di convenienza che ottiene il percorso dei file html tradotti

    >>> print html_path()
    /home/robby/Dropbox/Code/python/pymotw-it/html
    """
    return get_root(fixed_path=OLD_HTML_FOLDER)

def xml_path():
    """
    Metodo di convenienza che ottiene il percorso dei file xml tradotti
    
    >>> print xml_path()
    /home/robby/Dropbox/Code/python/pymotw-it/tran
    """
    return get_root(fixed_path=OLD_TRAN_FOLDER)

def get_xml_files():
    """
    Metodo di convenienza che estrae i percorsi completi dei file xml
    con la traduzione
    
    Modificare la variabile `OLD_TRAN_FOLDER` per impostare la directory
    dove sono contenuti i file
    """
    return [
        os.path.splitext(os.path.basename(f))[0]
        for f in os.listdir(xml_path())
        if f.endswith('.xml')
    ]

def get_html_files():
    """
    Metodo di convenienza che ritorna i percorsi completi dei file
    html con la traduzione

    Modificare la variabile `OLD_HTML_FOLDER` per impostare la directory
    dove sono contenuti i file
    """
    html_files = [
        os.path.splitext(os.path.basename(f))[0]
        for f in os.listdir(html_path())
        if f.endswith('.html') and not 'index' in f
    ]
    

def match_xml_html(output=False, sistema=False):
    """(bool, bool) -> list, list
    
    Confronto tra file xml ed html (evidenzia quelli non pubblicati)
    Rinomina i file xml ancora da pubblicare se `sistema` == `True`
    Ritorna i nomi dei file (senza suffisso) presenti nelle cartelle
    **tran** ed **html**
    """
    xml_files = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(xml_path())
                 if f.endswith('.xml')]
    html_files = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(html_path())
                 if f.endswith('.html') and not 'index' in f]
    if output:
        print "File xml  -> %d\nFile html -> %d" % (len(xml_files),  len(html_files))
    da_pubblicare = set.symmetric_difference(set(xml_files), set(html_files))
    if sistema:
        p = xml_path()
        for f in da_pubblicare:
            os.rename(os.path.join(p, f+'.xml'), os.path.join(p, f + ".da_tradurre"))
    return xml_files, html_files

def estrai_categoria_data():
    """
    Estrae la descrizione della categoria dai file html e ritorna
    un dizionario con chiave nome file (senza estensione) e valore la
    categoria rilevata e la data di ultima modifica
    """
    p = html_path()
    html_files = [os.path.join(p, f) for f in os.listdir(html_path())
             if f.endswith('.html') and not 'index' in f]
    retval = defaultdict(str)
    for f in html_files:
        categ = [riga.strip() for riga in open(f).readlines()
             if riga.startswith("<!-- Categoria")][0]
        categ = re.sub(r'[\<\>\-\!]', '', categ)
        retval[os.path.splitext(os.path.basename(f))[0]] = [
            categ.split(':')[1],
            datetime.date.fromtimestamp(os.path.getmtime(f))
        ]
    return retval
    
def scrivi_categoria_in_xml(elenco, diz_cat):
    xml_files = [os.path.join(xml_path(), f) 
                 for f in os.listdir(xml_path()) if f.endswith('.xml')]
    xml_dir = xml_path()
    for modulo in elenco:
        fn = os.path.join(xml_dir, modulo+'.xml')
        if not os.path.exists(fn):
            print "Articolo non presente: %s" % os.path.basename(fn)
            continue
        righe = open(fn).readlines()
        descr, vers = _estrai_da_tag(righe, 'descrizione')
        copy(fn, os.path.join(xml_dir,
                os.path.splitext(os.path.basename(fn))[0] + '.bak'))
        isinstance(diz_cat, dict)
        if diz_cat.get(modulo):
            righe.insert(1, "<categoria>%s</categoria>" % diz_cat[modulo][0])
            open(fn, mode='w').writelines(righe)
        else:
            print "Modulo %s non corrisponde" % modulo
        #print modulo, descr, vers
        
def _estrai_da_tag(righe, nome_tag, ripeti=False):
    """(list of str, str [,bool]) -> list of str
    
    Scansione `righe` e ritorna il testo racchiuso tra `tag` 1 sola volta
    se `ripeti` == `True`
    
    Da utilizzare per recuperare valori di tag univoci tipo descrizione
    """
    nome_tag = "%s" % nome_tag
    retval = []
    is_aperto = False
    for riga in righe:
        if riga[1:].startswith(nome_tag):
            if not is_aperto:
                is_aperto = True
        elif riga[2:].startswith(nome_tag):
            is_aperto = False
            if not ripeti:
                return retval
        else:
            if is_aperto:
                retval.append(riga.strip())
    return retval            
        
def ottieni_titolo_categ_descriz():
    """
    Ritorna un dizionario con chiave nome modulo che contiene:
    
    - data ultima modifica
    - titolo
    - versione
    - descrizione
    """
    retval = {}
    da_elaborare = get_xml_files()
    xml_dir = xml_path()
    for modulo in da_elaborare:
        fn = os.path.join(xml_dir, modulo+'.xml')
        if not os.path.exists(fn):
            print "Articolo non presente: %s" % os.path.basename(fn)
            continue
        righe = open(fn).readlines()
        descr, vers = _estrai_da_tag(righe, 'descrizione')
        titolo = " ".join(_estrai_da_tag(righe, 'titolo_1'))
        ultimo_agg = datetime.date.fromtimestamp(os.stat(fn).st_mtime)
        retval[modulo] = {  
            'descr': descr,
            'titolo': titolo,
            'agg': ultimo_agg,
            'versione': vers,
        }
    return retval

if __name__ == '__main__':
    print __doc__
    #match_xml_html(True, True) 

    #print estrai_categoria_data()
    #scrivi_categoria_in_xml(match_xml_html()[0], estrai_categoria_data())
    print ottieni_titolo_categ_descriz()