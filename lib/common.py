 #!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Utility varie 
Versione %s %s
""" % ( __version__, __date__ )

from os import name
import sys 
import os.path 
import datetime
import re

sys.path.append(r'../database')

PATHS = {
    'posix': r'/home/robby',
    'mac':  r'/Users/robby',
    'win32': r'c:\users\robby',
}

OLD_HTML_FOLDER = r'Dropbox/Code/python/pymotw-it/html'
OLD_TRAN_FOLDER = r'Dropbox/Code/python/pymotw-it2.0/tran'

OLD_TRAN_FOLDER3 = r'Dropbox/Code/python/pymotw-it3.0/tran'

def clear_console():
    """Lancia il comando di pulizia console per le 3 principali
    piattaforme
    """
    cmds = {
        'linux2': 'clear',
        'darwin': 'clear',
        'win32': 'cls',
    }
    platf = sys.platform
    if platf in cmds:
        os.system(cmds[platf])

def get_root(paths=PATHS, fixed_path=''):
    """
    Ritorna la radice del percorso di lavoro in base al sistema
    operativo in cui viene eseguito lo script, scegliendo tra i
    valori in `paths`
    
    >>> get_root()
    '/home/robby/'
    >>> print get_root(fixed_path='subfolder/subfolder1')
    /home/robby/subfolder/subfolder1
    """
    if sys.platform == 'darwin':
        return os.path.join(paths['mac'], fixed_path )
    if name in paths.keys():
        return os.path.join(paths[name], fixed_path )
    else:
        return os.path.join('.', fixed_path)


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
    return get_root(fixed_path=OLD_TRAN_FOLDER3)

def get_xml_files(nome_modulo=None):
    """([str]) -> list
    Metodo di convenienza che estrae i percorsi completi dei file xml
    con la traduzione
    
    Se `nome_modulo` è valorizzato recupera solo i file il cui nome
    contiene `nome_modulo` altrimenti recupera tutti i file .xml
    
    Modificare la variabile `OLD_TRAN_FOLDER` per impostare la directory
    dove sono contenuti i file
    """
    if nome_modulo:
        return [
            os.path.splitext(os.path.basename(f))[0]
            for f in os.listdir(xml_path())
            if f.endswith('.xml') and nome_modulo in f
        ]
    else:
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

def my_title(frase):
    """(str) -> str
    
    Capitalizzazione delle parole di una frase a ragion veduta (nel senso
    che non vengono rese maiuscole tutte le parole di una frase, le
    preposizioni e gli articoli)
    
    TODO: Sicuramente funzione imperfetta da verificare più accuratamente
    """
    non_capitalizzare = (
        'di da in con su per tra fra il la lo gli uno uno una del dello della degli dei al allo agli alle ed od'
    )
    l = []
    for parola in frase.split():
        if len(parola) == 1:
            pass
        elif parola in non_capitalizzare:
            pass
        else:
            parola = parola.title()
        l.append(parola)
    return " ".join(l)
    
def _estrai_da_tag(righe, nome_tag, ripeti=False):
    """(list of str, str [,bool]) -> list of str
    
    Scansione `righe` e ritorna il testo racchiuso tra `tag` 
    Se `ripeti` == `False` ritorna non appena individua la prima occorrenza
    di `nome_tag`
    
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

RE_CATEGORIA = re.compile(r'<categoria>(.*)</categoria>')
def _ottieni_categoria(righe):
    for riga in righe:
        match = RE_CATEGORIA.match(riga)
        if match and len(match.groups()) == 1:
            return match.groups()[0]
    return None

RE_INDICIZZA = re.compile(r'<indicizza>(.*)</indicizza>')
def _is_da_indicizzare(righe):
    for riga in righe:
        match = RE_INDICIZZA.match(riga)
        if match and len(match.groups()) == 1:
            valore = match.groups()[0]
            if valore and valore == "no":
                return False
    return True

            
RE_DATA_ARTICOLO = re.compile(r'<data_articolo>(.*)</data_articolo>')
def _ottieni_data_articolo(righe):
    for riga in righe:
        match = RE_DATA_ARTICOLO.match(riga)
        if match and len(match.groups()) == 1:
            return match.groups()[0].strip()
    return None
        
def ottieni_modulo(nome_modulo):
    modulo = get_xml_files()[0]
    xml_dir = xml_path()
    fn = os.path.join(xml_dir, nome_modulo+'.xml')
    if not os.path.exists(fn):
        print "Articolo non presente: %s" % os.path.basename(fn)
        return None
    return _ottieni_modulo(fn)

def _ottieni_modulo(nome_file):
    """(str) -> dict
    
    Legge `nome_file` e recupera i tag che contengono le info:
    
    - descrizione modulo
    - titolo
    - data aggiornamento (ultima data accesso al file)
    - versione traduzione
    - categoria
    """
    righe = open(nome_file).readlines()
    if not righe:
        return None
    try:
        descr, vers = _estrai_da_tag(righe, 'descrizione')
    except ValueError:
        descr, vers = '', ''
    titolo = " ".join(_estrai_da_tag(righe, 'titolo_1'))
    categ = _ottieni_categoria(righe).strip()
    data_articolo = _ottieni_data_articolo(righe)
    if not categ:
        print os.path.basename(nome_file), " manca categoria"
        categ = 'Sconosciuta'
    ultimo_agg = datetime.date.fromtimestamp(os.stat(nome_file).st_mtime)
    indicizza = _is_da_indicizzare(righe)
    if '-' in titolo:
        nome_modulo, titolo =  titolo.strip().split('-', 1)
    else:
        nome_modulo = titolo
    return {
        'descr': descr,
        'nome_modulo': nome_modulo,
        'titolo': titolo,
        'agg': ultimo_agg,
        'versione': vers,
        'categ': categ,
        'data_articolo': data_articolo,
        'indicizza': indicizza,
    }
        
def ottieni_moduli_tradotti():
    """Ritorna un dizionario con chiave nome modulo che contiene:
    
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
        retval[modulo] = _ottieni_modulo(fn)
        
    return retval

def accenti2entity(val):
    """(str) -> str
    
    Sostituisce le vocali accentate in `val` con le corrispondenti entità
    xml
    
    >> accenti2entity("il colibrì è un volatile")
    >> 'il colibr&igrave; &egrave un volatile
    """
    


if __name__ == '__main__':
    print __doc__
    print ottieni_moduli_tradotti()