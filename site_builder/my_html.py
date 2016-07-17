#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__=''
__version__='0.1'
__doc__="""Metodi per la costruzione di codice html per le pagine di
moduli ed indice
Versione %s %s
""" % ( __version__, __date__ )

from inline_sub import InlineSubs
from collections import namedtuple
from ast import literal_eval
from pyg import colora_codice

class MyHtml(object):
    """Si occupa della costruzione di elementi HTML"""
    insubs = InlineSubs()
    AUTOCLOSING_TAGS = (
        'br',
        'hr',
    )
    
    def _get_tag(self, tag_name, **kwargs):
        """(str [, **kvargs]) -> str
        
        Genera `tag_name` che non richiede elemento di chiusura, tipo hr/br
        Gli eventuali parametri sono gli attributi letterali del tag
        (Nessun controllo viene effettuato)
        
        _get_tag('br' class='classe') ritorna:
        <br class=classe />
        """
        return "<%s %s />" % (tag_name, self._get_attrs(dict(kwargs)))
    
    def _get_attrs(self, dic):
        """(dict) -> str
        
        Ritorna gli elementi in dict nella sintassi chiave='valore'
        
        Si utilizza per gestire gli attributi di un tag
        """
        if not dic:
            return ''
        attrs = ['']
        for k, v in dic.iteritems():
            if 'class' in k:
                k = 'class'
            attrs.append("%s='%s'" % (k, v))
        return ' '.join(attrs)    
    
    def _get_start_end_tag(self, tag_name, value='', **kwargs):
        """(str, str [**wkargs]) -> str

        Genera il tag HTML `tag_name` ed il suo contenuto
        Gli eventuali parametri sono gli attributi letterali del tag
        (Nessun controllo viene effettuato)
        """
        return "<%s%s>%s</%s>" % (
            tag_name,
            self._get_attrs(dict(kwargs)),
            value,
            tag_name
        )

    def _convert(self, value, char_sep = ' '):
        """(object) -> str
        
        Se `value` è una stringa unisce gli elementi separandoli con uno
        spazio.
        
        Si utilizza in quanto il valore da rendere in html viene in genere
        passato attraverso una lista, ad esempio per generare elementi li
        oppure tabelle
        """
        if isinstance(value, basestring):
            pass
        elif isinstance(value, list) or isinstance(value,  tuple):
            value = char_sep.join(value)
        else:
            value = str(value)
        return MyHtml.insubs.rimpiazza(value)

    def _lista(self, value, is_ordered=False, **kwargs):
        assert isinstance(value, list) or isinstance(value, tuple)
        acc = []
        tag = "ul" if not is_ordered else "ol"
        for row in value:
            acc.append(self._get_start_end_tag(
                "li",
                self._convert(row),
                **kwargs
            ))
        return self._get_start_end_tag(tag, " ".join(acc))
    
    def _codice(self, value, **kwargs):
        return colora_codice(value)

    def _codice_sql(self, value, **kwargs):
        return colora_codice(value, lexer_name='sql')

    def _codice_xml(self, value, **kwargs):
        return colora_codice(value, lexer_name='xml')

    def _codice_con_numerazione(self, value, **kwargs):
        return colora_codice(value, numera_righe=True)

    def _codice_xml_con_numerazione(self, value, **kwargs):
        return colora_codice(value, numera_righe=True, lexer_name='xml')

        
    def _vedi_anche(self, lista, dd_class=None, **kwargs):
        """(list [,str]) ->
        
        Rappresentazione di riferimenti bibliografici e interconnessioni
        
        Si estrinseca in una definition list con definizione il link
        della risorsa e descrizione la descrizione della risorsa medesima
        
        `dd_class` è un eventuale codice css da applicare al tag *dd*
        
        Precondizione: `value` deve essere una lista i cui valori, separati
        dal carattere **pipe** rappresentano rispettivamente:
        
        - url
        - descrizione url
        - descrizione risorsa
        
        l'ultimo valore può anche mancare, in tal caso viene recuperato
        dalla descrizione dell'url
        """
        assert isinstance(lista, list)
        Biblio = namedtuple('Biblio', 'url,desc,definiz')
        output = [""]
        ddargs = {}
        if dd_class:
            ddargs['class'] = dd_class
        for riga in [riga.split("|") for riga in lista if riga]:
            if len(riga) == 2:
                riga.append("")
            if len(riga) !=  3:
                print "Riga bibliografica malformata !!\n", riga
                continue
            biblio = Biblio(*riga)
            u = self.a(biblio.url, biblio.desc)
            output.append(self._get_start_end_tag('dt', u))
            output.append(self._get_start_end_tag('dd', biblio.definiz, **ddargs))
        output.append("")
        return self._get_start_end_tag('dl',"\n".join(output))
            
    # --------------------------------------------------------------------
    # METODI DI CONVENIENZA PER IL RENDERING DI SPECIFICI TAGS
    # I consumatori della classe dovrebbero utilizzare solo questi metodi
    # --------------------------------------------------------------------
    
    def h1(self, value, **kwargs):
        return self._get_start_end_tag('h1', self._convert(value), **kwargs)

    def h2(self, value, **kwargs):
        return self._get_start_end_tag('h2', self._convert(value), **kwargs)
    
    def h3(self, value, **kwargs):
        return self._get_start_end_tag('h3', self._convert(value), **kwargs)

    def h4(self, value, **kwargs):
        return self._get_start_end_tag('h4', self._convert(value), **kwargs)

    def h5(self, value, **kwargs):
        return self._get_start_end_tag('h5', self._convert(value), **kwargs)

    def p(self, value, **kwargs):
        return self._get_start_end_tag('p', self._convert(value), **kwargs)

    def strong(self, value, **kwargs):
        return self._get_start_end_tag('strong', self._convert(value), **kwargs)

    def section(self, id, value='', **kwargs):
        kwargs['id'] = "%s" % id
        return self._get_start_end_tag('section', value, **kwargs)

    def a(self, url, value, **kwargs):
        kwargs['href'] = "%s" % url
        return self._get_start_end_tag('a', value, **kwargs)

    def a_name(self, id, value='', **kwargs):
        kwargs['name'] = id
        return self._get_start_end_tag('a', value, **kwargs)
    
    def ul(self, value, **kwargs):
        return self._lista(value, is_ordered=False, **kwargs)

    def ol(self, value, **kwargs):
        return self._lista(value, is_ordered=True, **kwargs)
    
    def code(self, value, **kwargs):
        pigmentato = self._codice(value)
        return self._get_start_end_tag('div', pigmentato, **kwargs)

    def code_sql(self, value, **kwargs):
        pigmentato = self._codice_sql(value)
        return self._get_start_end_tag('div', pigmentato, **kwargs)

    def code_xml(self, value, **kwargs):
        pigmentato = self._codice_xml(value)
        return self._get_start_end_tag('div', pigmentato, **kwargs)


    def code_with_lineno(self, value, **kwargs):
        pigmentato = self._codice_con_numerazione(value)
        return self._get_start_end_tag('div', pigmentato, **kwargs)
    
    def code_xml_with_lineno(self, value, **kwargs):
        pigmentato = self._codice_xml_con_numerazione(value)
        return self._get_start_end_tag('div', pigmentato, **kwargs)
    
    
    def output_console(self, value, **kwargs):
        """(str) -> str
        
        Mostra l'output console"""
        testo = self._convert(value, "\n")
        return self._get_start_end_tag('pre', testo, **kwargs)
    
    def biblio(self, value, dd_class='indent', **kwargs):
        header = self.p(self.strong('Vedere anche:'))
        dl = self._vedi_anche(value, dd_class)
        return self._get_start_end_tag('div', header + dl, **kwargs)    
    
    def td(self, values, is_header=False, **kwargs):
        output = []
        splitchar = ";"
        if 'splichar' in kwargs:
            splitchar = kwargs['splitchar']
        tag = 'td' if not is_header else 'th'
        for value in values.split(splitchar):
            output.append(self._get_start_end_tag(
                tag, value=value, **kwargs
            ))
        return "\n".join(output)
    
    def tr(self, value,  **kwargs):
        return self._get_start_end_tag('tr', value, **kwargs)
    
    def table(self, values, **kwargs):
        """(list of lists) -> str
        
        Compone una tabella; ogni elemento in `values` è una lista
        """
        rows = []
        if 'with_header' in kwargs:
            with_header = True
        for i, row in enumerate(values):
            if with_header and i == 0:
                rows.append(self.tr(self.td(row, True)))
            else:
                rows.append(self.tr(self.td(row)))
        return self._get_start_end_tag('table', "\n".join(rows), **kwargs)
    
    def dl(self, values, dd_class=None, **kwargs):
        """(list of str) -> str
        
        Genera una definition list
        
        Precondizione: values è una lista di stringhe che contengono i valori
        del termine e della definizione dell'elemento separati da `|`
        """
        output = [""]
        ddargs = {}
        if dd_class:
            kwargs['class'] = dd_class
        for dt, dd in [riga.split("|") for riga in values]:
            output.append(self._get_start_end_tag('dt', dt))
            output.append(self._get_start_end_tag('dd', dd, **kwargs))
        output.append("")
        return self._get_start_end_tag('dl',"\n".join(output))
        
    
    
    
    def _alerts(self, value, **kvargs):
        """(list|str) -> str
        
        Genera il div per rendere gli alert, che possono essere:
        - info (azzurro)
        - warning (giallo)
        - success (verde)
        - danger (rosso)
        """ 
        return self._get_start_end_tag(
            'div',
            self._convert(value),
            **kvargs
        )
        
    def warning(self, value, **kwargs):
        """Metodi di convenienza che ottiene un box di avvertimento"""
        return self._alerts(value, class_='alert alert-warning')

    def note(self, value, **kwargs):
        """Metodi di convenienza che ottiene un box di informazioni"""
        return self._alerts(value, class_='alert alert-info')
    
    
if __name__ == '__main__':
    print __doc__
    h = MyHtml()
    print h.h3('tag h3', id=123)
    print h.h1('tag h1')
    #print h.a('www.python.org', 'Python!', title='sito python')
    #print h.a_name('tag a name')
    lista = [
        'http://docs.python.org/library/abc.html|abc|La documentazione della libreria standard per questo modulo', 
        'http://www.python.org/dev/peps/pep-3119|PEP 3119|Introduzione alle classi base astratte', 
        'http://docs.python.org/library/collections.html|collections|La documentazione della libreria standard per le collezioni'
    ]
    #print h._vedi_anche(lista)
    
    l = (
        ('qui', 'pippo', 'ciccio di nonna papera'),
        ('snoopy', 'lucy', 'charlie'),
    )
    print h.table(l)