#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os.path
import codecs
import re
from functools import partial
from shutil import copyfile
from django.utils.encoding import smart_text
import my_html
from comprimi_esempi import comprimi
from inline_sub import InlineSubs


__date__='02/07/2017'
__version__='2.1'

__doc__ = """

Note sui file di traduzione da elaborare
========================================

Quando ho iniziato avevo pochissima esperienza in python

Il file da elaborare è in formato pseudo xml, non è ben formato e
contiene tag che **NON** devono essere elaborati in quanto rappresentano
codice di esempio quindi non mi avvalgo di alcun modulo che elabori
file xml tipo lxml o BeautifulSoup.

I file sono stati così creati in
quanto il progetto è individuale e volevo un file sorgente abbastanza
leggibile e facile da elaborare. La condizione fondamentale, infatti,
è che ogni tag che rappresenta una porzione di testo da rendere in
HTML sia sempre da solo **ad inizio riga**

Versione %s %s
""" % (__version__, __date__ )


h = my_html.MyHtml()  # Si occupa del rendering in HTML dei dati

DEF_CHARSET = 'utf-8'

TESTSDIR = os.path.abspath(os.path.dirname(__file__))
TEST_XML_FILE = r'/home/robby/Dropbox/Code/python/pymotw-it/tran/abc.xml'
HTML_OUTPUT = 'xmt2html_test.html'
RE_TAG_START = re.compile(r'^<\w+>')
RE_TAG_END = re.compile(r'^<\/\w+>')
RE_STRIP_TAG = re.compile(r'[<>/]')


# Lista dei tag - serve ad is_my_tag() per accertarsi di avere trovato un 
# MIO tag e non un pezzo di codice od altro I valori sono funzioni parziali
# per le quali viene valorizzata la parte relativa alla gestione css
MY_TAGS = {
    'avvertimento': partial(h.warning),
    'categoria': None, 
    'descrizione': None,
    'deflist': partial(h.dl),
    'incipit': None, 
    'inserito_il': None, 
    'lista': partial(h.ul),
    'lista_ordinata': partial(h.ol),
    'lista_ricorsiva': partial(h.ul),
    'mk_xml_code': partial(h.code_xml, class_='well pre-scrollable'),
    'mk_xml_code_lineno': partial(
        h.code_xml_with_lineno,
        class_='well pre-scrollable'
    ),
    'note': partial(h.info),
    'success': partial(h.success),
    'danger': partial(h.danger),
    'py_code': partial(h.code, class_='well pre-scrollable'),
    'py_code_lineno': partial(h.code_with_lineno, class_='well pre-scrollable'),
    'py_output': partial(
        h.output_console,
        class_='well pre-scrollable console',
        script_folder='/home/robby/Dropbox/Code/python/pymotw-it3.0/dumpscripts'
    ),
    'sottotitolo': partial(h.h4),
    'sql_code': partial(h.code_sql, class_='well pre-scrollable'),
    # 'tabella_semplice': partial(h.table, with_header=True, class_='table'),
    'tabella_1': None,
    'testo_normale': partial(h.p), 
    'titolo_1': None,
    'titolo_2': partial(h.h2),
    'titolo_3': partial(h.h3),
    'titolo_4': partial(h.h4),
    'vedi_anche': partial(h.biblio, class_='well'),
    'indicizza': None,
    'tabella_semplice': partial(
        h.table,
        with_header=True,
        class_='table table-responsive table-bordered table_striped table-hover'
    )
}

MY_TAG_KEYS = MY_TAGS.keys()


def is_my_tag(tag):
    """(str) -> bool
    
    Cerca `tag` nella lista dei tag ammessi, ritorna True se trovato dopo
    avere tolto le parentesi angolari
    
    Precondizione: `tag` deve essere *lowercase*
    """
    return re.sub(r'>|<|/', '', tag.strip()) in MY_TAG_KEYS


def pulisci_tag(tag):
    """(str) -> str
    
    Pulisce `tag` per ottenere il nome del tag senza parentesi
    """
    assert isinstance(tag, basestring)
    return RE_STRIP_TAG.sub('', tag.strip())


entities = {"à": "&agrave;", "è": "&egrave;", "ì": "&igrave;", "ò": "&ograve;",
            "ù": "&ugrave;"}


def text2entity(file_name):
    log = []
    if not os.path.exists(file_name):
        raise IOError("Manca " + file_name)    
    copyfile(file_name, file_name + ".bak")
    buf = open(file_name, "r").read()
    for k,v in entities.iteritems():
        log.append( "Sostituzione di %s con %s " % (k,v))
        buf = buf.replace(k,v)
    open(file_name, 'w').write(buf)    
    return "\n".join(log)


def load(xml_file, dir_esempi, log, builder_conf):
    """(str, str, :class InlineSubs:, str) -> list of dict
    
    Legge il contenuto di ``xml_file`` filtrando le righe con commenti.

    Ritorna:
    
    - una lista composta da dizionari:
        - chiave -> contiene il nome del tag
        - buffer -> contiene le righe da trasporre in html con il tag chiave
    - un flag per indicizzazione
    - l'elenco dei file di esempio dell'articolo

    Prerequisito: Tutti i tag per l'estrazione degli elementi sono di
    apertura e chiusura e **devono** essere da soli su di una sola riga.
    
    Sono ammessi tag di commento a patto che si trovino su di una sola riga
    """
    seq_elementi = list()  # Conterrà elementi di dizionario 'tag': righe
    buf = list()  # Le righe da assegnare ad un tag ancora aperto
    is_aperto = False  # Se true la riga viene aggiunta al buffer del tag
    tag = ''  # conserva il nome del tag da utilizzare come chiave nel diz
    righe = list()
    indicizza = None

    for i, riga in enumerate([riga.rstrip() for riga in
                             codecs.open(xml_file, encoding='utf-8')
                             if riga and not riga.startswith('<!--')]):
        if RE_TAG_START.match(riga) and is_my_tag(riga.lower()):
            if 'indicizza' in riga:
                indicizza = True
            is_aperto = True
            tag = pulisci_tag(riga.lower())
        elif RE_TAG_END.match(riga) and is_my_tag(riga.lower()):
            if tag in builder_conf['code_tags'] and len(buf) == 1:
                buf = _get_codice_di_esempio(buf, dir_esempi, log)
            elif tag == 'testo_normale':
                _norm_testo_normale(buf)
            elif tag in builder_conf["output_tags"]:
                _norm_output(buf)
            seq_elementi.append({'tag': tag, 'buffer': buf, 'row':  i})
            buf = []
            tag = ''
            is_aperto = False
        else:
            if is_aperto:
                buf.append(riga)
    # Visto che i tag sono sempre di apertura/chiusura non mi preoccupo
    # di svuotare il buffer
    file_esempio = _get_file_esempio(seq_elementi)
    return seq_elementi, indicizza, file_esempio


PUNTEGGIATURA = ('.', ';', ':')


def _get_file_esempio(seq_elementi):
    """Cerca nel codice di esempio (tag: py_code) il nome del file

    **precondizione** il file di esempio deve avere una riga con il nome del
    file commentata

    :param seq_elementi: gli elementi che costituiscono la pagina da rendere
    :return: la lista con i nomi dei file di esempio trovati
    """
    files = []
    for elemento in seq_elementi:
        if not elemento['tag'] == 'py_code':
            continue
        for line in elemento['buffer']:
            if not line.startswith("#"):
                continue
            if line.find('.py') < 0:
                continue
            end = line.index('.py')
            filename = line[0:end + 3].split()[-1]
            files.append(filename)
            break
    return files


def _norm_testo_normale(buf):
    """(list of str)

    Verifica se l'ultimo carattere della lista  un carattere di punteggiatura.
    In caso contrario aggiunge un punto (assumendo che, trattandosi di un
    paragrafo sia la punteggiatura più probabile se non fornita
    """
    if buf and not buf[-1].strip().endswith(PUNTEGGIATURA):
        buf[-1] += "."


ENTITIES = {
    '<': '&lt;',
    '>': '&gt;'
}


def _norm_output(buf):
    """(list of str)

    Sostituisce caratteri che non vengono resi dal motore html nelle
    corrispondenti entità
    """
    for i, row in enumerate(buf):
        to_sub = []
        for key in ENTITIES.keys():
            if key in row:
                to_sub.append(key)
        for char in to_sub:
            buf[i] = buf[i].replace(char, ENTITIES[char])
    return buf


def _get_codice_di_esempio(buf, dir_esempi, log):
    """(list, str, list) -> list

    Parse di `buf` per vedere se esiste un file che corrisponde al testo, che
    viene letto ed il contenuto restituito

    Se `buf` contiene più di un elemento viene ritornato *as is*

    :param buf: il testo da esaminare
    :param dir_esempi: la directory dove si trova l'eventuale esempio
    :param log:
    :return: il testo originale oppure il contenuto del file raggpresentato
             da `buf`
    """
    if len(buf) > 1:
        return buf
    if not buf[0].startswith(("#", "<")):
        return buf
    try:
        _, filename = re.split(r'\s+', buf[0].strip(), 2)
        with open(os.path.join(dir_esempi, filename)) as fh:
            return [row.rstrip() for row in fh.readlines()]
    except:
        prompt = "Fallita importazione del codice di esempio per %s" % buf[0]
        log.append(prompt)
        return buf


def check_my_tags(seq_elementi):
    """(dict) -> list of string
    
    Verifica se la chiave 'tag' in `seq_elementi` è un tag riconosciuto per
    la conversione in html. Ritorna una lista degli elementi non trovati
    
    Utilizzare prima di costruire la pagina per verificare errori di
    sintassi dei tag del file xml
    """
    not_found = []
    for item in seq_elementi:
        tag = item['tag']
        if not is_my_tag(tag):
            not_found.append(tag)
    return not_found


# In produzione questo sparisce
TEMP_FATTI = ('titolo_2', 'titolo_3', 'titolo_4', 'testo_normale',
              'lista', 'py_code', '', 
              'py_output', 'vedi_anche', 'tabella_semplice', 'mk_xml_code', 
              'avvertimento', 'note', 'titolo_3', 'deflist', 'sql_code', 
              'sottotitolo', 'lista_ricorsiva', 'py_code_lineno',
              'mk_xml_code_lineno', 'lista_ordinata')

CHECK_SYNTAX = ('titolo_2', 'titolo_3', 'titolo_4', 'testo_normale',
                'lista', '',
                'tabella_semplice',
                'avvertimento', 'note', 'titolo_3', 'deflist',
                'sottotitolo', 'lista_ricorsiva',
                'lista_ordinata')


def _is_for_syntax(tag, tags=CHECK_SYNTAX):
    return tag.lower() in tags


def _raccogli_per_check_sintassi(tag,  row,  text,  check_sintassi):
    if _is_for_syntax(tag):
        check_sintassi.append( { 'row': row, 'text': striphtml(text) } )


def prepara_articolo(seq_elementi, tag_ind=('titolo_2', 'titolo_3'), log=None):
    """(list of str, tuple of str) -> list, list
    
    Prepara il codice html per la pagina del modulo
    
    Ritorna:
    
    - il codice per l'indice nella barra destra
    - il codice per il contenuto dell'articolo
    - Il testo per la verifica della sintassi
    """
    indice = []
    contenuti = []
    check_sintassi = []
    prg = 0
    for item in seq_elementi:
        tag = item['tag']
        if is_my_tag(tag):
            _raccogli_per_check_sintassi(
                tag, item['row'], item['buffer'], check_sintassi
            )
            if tag in tag_ind:
                item['a_name'] = h.a_name(str(prg))
                b = " ".join(item['buffer'])
                # if '3' in tag:
                #     b = "&nbsp;&nbsp;&nbsp;&nbsp;" + b
                indice.append(
                    h.a("#"+str(prg), smart_text(b, encoding='utf-8'))
                )
                contenuti.append(h.section(str(prg)))
                prg += 1
            if tag in TEMP_FATTI:
                codice = MY_TAGS[tag](item['buffer'])
                contenuti.append(codice)
            else:
                # print("{0} {1}".format(tag, "da gestire"))
                if log:
                    log.append("{0} {1}".format(tag, "non gestito"))
        else:
            print(tag)
    return indice, contenuti, check_sintassi   

            
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', smart_text(data, encoding='utf-8'))


def render_articolo(file_xml, example_folder, zip_folder, tag_ind,
                    log=None, builder_conf=None):
    """(str) -> list, list
    
    Prepara il file html con l'articolo per il modulo contenuta in
    `file_xml`
    """
    seq_elementi, indicizza, lista_esempi = load(file_xml, example_folder,
                                                 log, builder_conf)
    outfile = os.path.splitext(os.path.basename(file_xml))[0]
    file_compresso = None
    if not lista_esempi:
        log.append("Nessun file di esempio trovato per il modulo")
    if lista_esempi:
        file_compresso, not_found = comprimi(example_folder, lista_esempi,
                                             zip_folder, outfile)
        if isinstance(log, list):
            if not_found:
                prompt = "I seguenti file esempio non sono stati trovati\n"
                prompt += '\n'.join([fn for fn in not_found])
                log.append(prompt)
            log.append("{0} file di esempio compressi in {1}".format(
                len(lista_esempi), os.path.abspath(file_compresso)))
    indice_articolo, contenuti, chk_sintassi = prepara_articolo(
        seq_elementi, builder_conf['tag_summary'], log
    )
    return indice_articolo, contenuti, indicizza, chk_sintassi, file_compresso


# def test_partial():
#     h2 = functools.partial(h.h2)
#     print h2("testo h2")

if __name__ == '__main__':
    c = ['Rig<a>1', '<Riga2', 'riga:']
    print(_norm_output(c))
    # test_partial()
