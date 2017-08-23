#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

__date__=''
__version__='0.1'
__doc__="""
Il punto di entrata dell'applicazione (nella modalità console)

Da qui vengono costruite le singole pagine, gli indici e le tabelle
riepilogative

Le pagine vengono costruite basandosi su bootstrap 3

I tipi di pagine che possono essere costruite sono:

pagine riepilogative con teasers (:py:func:`crea_pagine_indice`)
    sono le pagine che contengono gli incipit dei moduli (12 per pagina), dalle
    quali si può accedere al dettaglio del singolo modulo

pagina modulo
    la pagina che descrive il modulo (se ne possono costruire anche in batch)

pagine indice (:py:func:`crea_tabella_indice`)
    le pagine che riepilogano tutti i moduli presenti

Argomenti della versione console:

- Nessun argomento: ricostruzione di tutti i moduli (dopo conferma)
- Se il primo argomento inizia con ind si ricostruisce la pagina indice
- Se il primo argomento inizia con tab si ricostruisce la tabella riepilogativa
- qualsiasi altra stringa iniziale rappresenta il nome di un modulo da costruire,
  se ne possono passare diverse separate da virgola


Versione %s %s
""" % ( __version__, __date__ )

try:
    import glob
    import codecs
    import os.path
    import os
    import sys
    import datetime
    import traceback
    import urlparse
    from collections import defaultdict
    from math import ceil
    #import django
    #django.setup()
    from django import template
    from django.template import loader

    from dj_indice import Indice
    from dj_modulo import DjModulo
    from dj_tabelle_indici import DjTabelleIndici
    from modulo import Modulo, elenco_per_indice
    import modulo_xml2html
    from index_builder import ottieni_tabella
    sys.path.append(r'../lib')
    from common import clear_console, my_title
    from footer import Footer
    from rss_feed_builder import Feed, FeedItem
    import spell_checker as  sc
except ImportError as imperr:
    raise Exception("Errore importazione modulo\n\n" + imperr.message)


# TODO: Trasferire su file di configurazione la gestione dei parametri
DEF_CHARSET='utf-8'
TEMPLATE_DIRS = ['../templates']
ZIP_FILES_DIR = r'../html/examples'
EXAMPLES_DIR = r'../dumpscripts'
TRAN_DIR = r'../tran'
TEMPLATE_INDEX_NAME = 'index.html'
TEMPLATE_MODULE_NAME = 'modulo.html'
TEMPLATE_REF_NAME = 'ref.html'
TEMPLATE_TABALFA_NAME = 'tabella_moduli.html'
HTML_DIR = r'../html'
INDICE_MODULI_PER_PAGINA = 12
FILE_INDICE = 'index'
HTML_EXT = '.html'
TEST_XML_FILE = r'/home/robby/Dropbox/Code/python/pymotw-it/tran/abc.xml'
FOOTER = Footer(
    'PyMOTW-it 3',
    periodo='2017',
    data_agg=datetime.date.today().strftime("%d-%m-%Y")
)
RSS_REMOTE_ROOT_FOLDER = r'http://robyp.x10host.com/3/'
RSS_FEED_NAME = r'pymotw-it3_feed.xml'
RSS_FEED_TITLE = 'PyMOTW-it 3: Il modulo python della settimana'
RSS_FEED_DESCR = "Traduzione italiana di 'The Python 3 Module of the Week (http://pymotw.com/3/)"


def imposta_param_django(template_dirs):
    """(list of str)

    Imposta i parametri di configurazione per django ed assegna i
    percorsi per i file template in `template_dirs`
    """
    from django.conf import settings
    if  not settings.configured:
        settings.configure(
            DEBUG=True, TEMPLATE_DEBUG=True,
            TEMPLATE_DIRS=(template_dirs),
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.messages',
                ),
        )

def build(template_file, context_dict, rendered_file):
    """(str, dict, str)

    Rendering in `rendered_file` dalla pagina template `template_file`
    utilizzando gli elementi in `context`
    """
    try:
        t = loader.get_template(template_file)
        open(rendered_file, mode='w').write(
            codecs.encode(t.render(
                template.Context(context_dict)), DEF_CHARSET)
        )
    except Exception as ex:
        print traceback.format_exc()


def _chunks(l, n):
    """(list, int) -> list

    Ritorna blocchi di `n` elementi in `l`
    """
    return [l[i:i+n] for i in range(0, len(l), n)]


def _categorie_per_indice(elenco_moduli):
    """(list of :py:class:`Modulo`) -> list

    Scorre `elenco_moduli`, ottiene un dizionario per categoria di modulo che
    contiene i moduli appartenenti a detta categoria; quindi scorre il
    dizionario ordinato per chiavi e ritorna una lista formata da liste il
    cui primo elemento è il nome della categoria ed il secondo è una lista di
    tuple il cui primo valore è il nome del modulo ed il secondo l'indirizzo

    Serve per popolare la barra destra delle pagine indice (elenco moduli per
    categorie)
    """
    dd = defaultdict(list)
    for modulo in elenco_moduli:
        isinstance(modulo, Modulo)
        dd[my_title(modulo.categoria)].append((modulo.nome, modulo.url))
    l = []
    for k in sorted(dd.iterkeys()):
        l.append((k, dd[k]))
    return l


def crea_pagine_indice(template_name, file_indice, mod_per_pagina, footer):
    """(str, str)

    Crea le pagine indice, che contengono i teaser per 12 moduli ognuna
    """
    gm = []
    prg = 0
    ms =  elenco_per_indice()
    moduli =  sorted(ms, key=lambda x: x.nome.lower())
    categ_per_indice = _categorie_per_indice(moduli)

    #e = sorted(moduli, key=lambda x: x.nome)

    pagine = ceil(len(moduli) / mod_per_pagina)
    for gruppo_moduli in _chunks(moduli, mod_per_pagina):
        for m in gruppo_moduli:
            gm.append(m)
        i = Indice(gm, footer, categ_per_indice)
        if ((prg + 1) < pagine):
            i.prev_nr_page = prg + 1
        if (prg + 1 ) == 1:
            i.next_nr_page = int(pagine - 1)
        elif (prg + 1) < pagine:
            i.next_nr_page = prg - 1
        else:
            i.next_nr_page = int(pagine-2)

        dic = {'indice': i,}
        fn = '%s%s.html' % (file_indice, "_" + str(prg) if prg else '')
        build(template_name, dic, os.path.join(HTML_DIR, fn))
        prg += 1
        gm = []
    return


def crea_pagina_modulo(template_name, file_modulo, footer, log=None):
    """(str, str, str [, list])

    Crea la pagina per un modulo.

    - `template_name` è il nome del modello per il rendering
    - `file_modulo` è il file xml dal quale ricavare la pagina html
    - 'footer' un oggetto :py:class:`Footer` che contiene informazioni da inserire
      nel footer della pagina
    - `log` è una lista che conterrà le info di log rilasciate dai metodi che
      compongono la pagina
    """
    indice, main_content, is_ind, check_sintassi, zipfile = \
        modulo_xml2html.render_articolo(
            file_modulo, EXAMPLES_DIR, ZIP_FILES_DIR, log
        )
    fn = os.path.splitext(os.path.basename(file_modulo))[0]
    modulo = Modulo.ottieni_modulo(fn)
    m = DjModulo(indice, main_content, modulo, footer, zipfile)
    fn += '.html'
    dic = {'modulo': m,}
    build(template_name, dic, os.path.join(HTML_DIR, fn))
    return is_ind


def get_cronologia(file_cronologia="../cronologia.txt"):
    """(str) -> list of tuple

    Ottiene i dati relativi alla data di pubblicazione dei moduli
    """
    retval = []
    for riga in open(file_cronologia).readlines():
        if not riga or not riga[0].isdigit():
            continue
        data, temp = riga.strip().split(" ", 1)
        nome, junk = temp.split('-', 1)
        retval.append((data, nome.strip()))
    return retval


def abbina_cronologia(cronologia, moduli, data_fmt='%d.%m.%Y'):
    """(list of tuple, Modulo)

    Cerca la data di pubblicazione del modulo, aggiorna l'oggetto se la
    trova
    """
    for modulo in moduli:
        isinstance(modulo, Modulo)
        for data, nome in cronologia:
            nome_alias = nome.split(":")
            if nome_alias[0].lower() == modulo.nome.lower().replace('_', '.'):
                modulo.data_pub = datetime.datetime.strptime(data, data_fmt)
                if len(nome_alias) == 2:
                    modulo.nome_per_rss = nome_alias[1]
                else:
                    modulo.nome_per_rss = nome_alias[0]
                break
        if not modulo.data_pub:
            print modulo.nome
            print


def crea_feed_rss(base_path, outfile, title, description=''):
    """(list of tuple, str, str, str, str)

    Scrive un file rss per il sito
    """
    moduli = elenco_per_indice()

    abbina_cronologia(get_cronologia(), moduli)
    moduli_ordinati = Modulo.ordina_per_data(moduli)
    local_feed = os.path.join(HTML_DIR, outfile)
    outfile = urlparse.urljoin(base_path, outfile)
    feed = Feed(title, outfile, description)
    for modulo in moduli_ordinati:
        assert isinstance(modulo, Modulo)
        link_guid = urlparse.urljoin(base_path, modulo.url)
        item = FeedItem(
            title=modulo.nome_per_rss,
            lnk=link_guid,
            descr=modulo.descrizione,
            date=datetime.datetime.combine(
                modulo.data_pub, datetime.datetime.min.time(),
            ),
            guid=link_guid

        )

        feed.set_item(item)
    open(local_feed, mode='w').write(feed.get_feed())


def crea_tabella_indice(template_name):
    """(str)

    Crea la pagina che contiene la tabella che riepiloga tutti i moduli

    `template_name` è il nome del modello per il rendering
    """
    moduli = elenco_per_indice()
    #corpo = ottieni_tabella(moduli)
    m = DjTabelleIndici(moduli, FOOTER)
    fn = 'indice_alfabetico.html'
    dic = {'modulo': m,}
    build(template_name, dic, os.path.join(HTML_DIR, fn))


def _sintassi(pn):
    return '%s [ind|tab|<nome_modulo>]' % os.path.basename(pn)


def rebuild_all():
    crea_pagine_indice(
        TEMPLATE_INDEX_NAME,
        FILE_INDICE,
        INDICE_MODULI_PER_PAGINA,
        FOOTER
    )
    crea_tabella_indice(TEMPLATE_TABALFA_NAME)

    pattern =  "%s/*.xml" % TRAN_DIR
    for choice in glob.glob(pattern):
        if not os.path.exists(choice):
            exit(0)
        print "Costruzione pagina %s in corso ..." % os.path.basename(choice)
        if 'riferimenti_' in choice:
            is_ind =  crea_pagina_modulo(TEMPLATE_REF_NAME, choice, FOOTER)
        else:
            is_ind =  crea_pagina_modulo(TEMPLATE_MODULE_NAME, choice, FOOTER)
        #crea_pagina_modulo(TEMPLATE_MODULE_NAME, choice, FOOTER)


def pubblica(moduli):
    crea_pagine_indice(
        TEMPLATE_INDEX_NAME,
        FILE_INDICE,
        INDICE_MODULI_PER_PAGINA,
        FOOTER
    )
    crea_tabella_indice(TEMPLATE_TABALFA_NAME)


def _norm_path(modulo, def_dir, def_ext='.xml'):
    fn, ext = os.path.splitext(modulo)
    if not ext:
        ext = def_ext
    return os.path.abspath(os.path.join(def_dir, fn + ext))


def build_module(moduli):
    """Funzione principale per i consumatori del modulo

    :param moduli: una lista di moduli da rendere (percorso completo)
    """
    imposta_param_django(TEMPLATE_DIRS)
    log = []
    for modulo in moduli:

        modulo = _norm_path(modulo, TRAN_DIR)
        x = os.getcwd()
        if not os.path.exists(modulo):
            log.append("Modulo %s non trovato" % modulo)
            continue
        if 'riferimenti_' in modulo:
            is_ind = crea_pagina_modulo(TEMPLATE_REF_NAME, modulo, FOOTER, log)
        else:
            is_ind = crea_pagina_modulo(TEMPLATE_MODULE_NAME, modulo, FOOTER, log)
        log.append("Costruzione pagina %s terminata" % os.path.basename(modulo))
    return log


if __name__ == '__main__':
    print __doc__
    parms = sys.argv
    clear_console()
    # Per prima cosa si impostano i parametri per django
    imposta_param_django(TEMPLATE_DIRS)

    # Nessun parametro conferma per ricostruzione di tutti i moduli
    if len(parms) == 1:
        scelta = raw_input('Ricostruire tutto? (S/N)')
        if scelta and scelta[0].lower() == 's':
            rebuild_all()
        exit(0)
    dummy, choices = parms
    # Se il primo argomento inizia con ind si ricostruisce la pagina indice
    # ed il feed rss
    if choices.lower().startswith('ind'):
        crea_feed_rss(
            RSS_REMOTE_ROOT_FOLDER,
            RSS_FEED_NAME,
            RSS_FEED_TITLE,
            RSS_FEED_DESCR
        )
        crea_pagine_indice(
            TEMPLATE_INDEX_NAME,
            FILE_INDICE,
            INDICE_MODULI_PER_PAGINA,
            FOOTER
        )
    # Se il primo argomento inizia con tab si ricostruisce la tabella riepilogativa
    elif choices.lower().startswith('tab'):
        crea_tabella_indice(TEMPLATE_TABALFA_NAME)
    else:
        pubblica = False
        da_pubblicare = []
        if choices.lower().startswith('pubblica'):
            pubblica = True
            choices = choices[1:]

        # si possono indicare tanti moduli quanto desiderati senza estensione
        # ed intervallati da una virgola
        for choice in choices.split(','):
            if not os.path.splitext(choice)[1]:
                choice += '.xml'
                choice = os.path.join(TRAN_DIR, choice)
                print os.path.abspath(choice)
            if not os.path.exists(choice):
                choice = os.path.join(TRAN_DIR, choice)
                if not os.path.exists(choice):
                    print "Il modulo %s non è stato trovato" % choice
                    exit(-1)
                #continue
            if pubblica:
                da_pubblicare.append(choice)
            print "Costruzione pagina %s in corso ..." % os.path.basename(choice)
            if 'riferimenti_' in choice:
                is_ind =  crea_pagina_modulo(TEMPLATE_REF_NAME, choice, FOOTER)
            else:
                is_ind =  crea_pagina_modulo(TEMPLATE_MODULE_NAME, choice, FOOTER)
            print "Costruzione pagina %s terminata" % os.path.basename(choice)

        if is_ind:
            pubblica(da_pubblicare)


    print "Fine"
    #raw_input()
