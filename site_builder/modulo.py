#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Costruisce le pagine indice
Versione %s %s
""" % ( __version__, __date__ )

import sys
sys.path.append(r'../lib')
from common import ottieni_moduli_tradotti, ottieni_modulo
from inline_sub import InlineSubs

class Modulo(object):
    insubs = InlineSubs()
    def __init__(self, nome):
        self.nome = nome
        self.versione = None
        self.titolo = ''
        self.descrizione = ''
        self.data_agg = None
        self.url = nome + '.html'
        self.categoria = ''
        self.data_pub = None
        self.nome_per_rss = None
        self.indicizza = False
        self.titolo_ref = ''

    @property
    def nome_per_teaser(self):
        return self.nome.replace('_', ' ')
    
    


    @staticmethod
    def ottieni_modulo(nome_modulo):
        diz = ottieni_modulo(nome_modulo)
        m = Modulo(nome_modulo)
        m.nome = diz['nome_modulo']
        m.categoria = diz['categ']
        m.data_agg = diz['agg']
        m.descrizione = diz['descr']
        m.titolo = diz['titolo']
        m.versione = diz['versione']
        m.titolo_ref = m.titolo.split('-')[0]
        
        return m
    
    def per_tabella_indice(self):
        return [
            self.data_agg.strftime('%d.%m.%Y'),
            self.nome,
            self.titolo
        ]

    
    @staticmethod
    def ordina_per_data(moduli):
        moduli_ok =  [m for m in  moduli if m.data_pub]
        x = sorted(moduli_ok, key=lambda m: m.data_pub, reverse=True)
        for m in x:
            print  m.data_pub, m.nome
        return x

def elenco_per_indice():
    """Ritorna una lista di oggetti :py:class:`Modulo`"""
    elenco = []
    insubs = InlineSubs()
    for k, v in ottieni_moduli_tradotti().iteritems():
        if not v['indicizza']:
            continue
        modulo = Modulo(k)
        isinstance(modulo, Modulo)
        modulo.data_agg = v['agg']
        modulo.descrizione = insubs.rimpiazza(v['descr'])
        modulo.titolo = v['titolo']
        modulo.versione = v['versione']
        modulo.categoria = v['categ']
        modulo.indicizza = v['indicizza']
        elenco.append(modulo)
    #Modulo.ordina_per_data(elenco)
    return elenco
        