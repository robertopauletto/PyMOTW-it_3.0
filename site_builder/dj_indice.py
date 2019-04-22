#!/usr/bin/env python
# -*- coding: utf-8 -*-


__date__ = ''
__version__ = '0.2'
__doc__ = """Costruisce le pagine indice
Versione %s %s
""" % (__version__, __date__)


class Indice(object):
    base_url = 'index{}.html'
    moduli_per_riga = 3
    """
    Rappresenta una pagina indice con elenco moduli contenuti in ordine
    alfabetico
    """
    def __init__(self, elenco_moduli, footer, categ, page_no, tot_pages):
        """

        :param list elenco_moduli: i moduli per la pagina
        :param Footer footer: il footer della pagina
        :param list categ: le categorie da rendere in spalla dx della pagina
        :param int page_no: il numero pagina nell'ambito
        :param int tot_pages: numero totale pagine
        """
        self.moduli = elenco_moduli
        self.page = page_no
        self.footer = footer
        self.elenco_categorie = categ
        self.tot_pages = int(tot_pages)

    def get_prev_page(self, page):
        page -= 1
        if page <= 0:
            return self.tot_pages
        elif page == 1:
            return ''
        return page

    def get_next_page(self, page):
        page += 1
        return page if page <= self.tot_pages else ''

    @property
    def prev_url(self):
        page = self.get_prev_page(self.page)
        x = Indice.base_url.format('_' + str(page) if page else '')
        return x

    @property
    def next_url(self):
        page = self.get_next_page(self.page)
        x = Indice.base_url.format('_' + str(page) if page else '')
        return x

    @property
    def modulo_tre(self):
        """
        Ottiene una lista composta da liste di 3 oggetti
        `py:class:Modulo`
        """
        return [self.moduli[i:i+Indice.moduli_per_riga]
                for i in range(0, len(self.moduli), Indice.moduli_per_riga)]
