#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__='08-11-2013'
__version__='beta'
__doc__="""Generates HTML highlighted code listings for source code
files in any language known to pygments.
For a list of supported formats see http://pygments.org/languages/
by xhuman - Adattamento Roberto Pauletto
Versione %s %s
""" % ( __version__, __date__ )


import os
import sys
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter

# La classe Pyg viene rimpiazzata dalle funzioni sottostanti

def _get_lexer(lexer_name):
    """(str)
    
    Ottiene il lexer specificato da `lexer_name`
    """
    try:
        return get_lexer_by_name(lexer_name)
    except IndexError as ie:
        raise 'Errore: manca il lexer %s\n%s' % (lexer_name, ie.message)

def _prepara_testo(testo):
    """(object)
    
    Prepara il testo per la pigmentazione, di norma dovrebbe ricevere una
    lista o tupla di stringhe, ma adatta anche stringhe ed oggetti,
    (**NON RACCOMANDATO** a meno che l'oggetto abbia una rappresentazione
    stringa confacente allo scopo)
    """
    if isinstance(testo, list) or isinstance(testo, tuple):
        return "\n".join(testo)
    elif isinstance(testo, basestring):
        return testo
    else:
        return str(testo)
    


def colora_codice(testo, numera_righe=False, lexer_name='python'):
    """([str] [,str] [,str]) -> str
    Ottiene il pezzo di codice HTML formattato che racchiude il codice
    python 'colorato'.
    Opzionalmente incapsula detto codice in un tag div prescelto
    """
    formatter = HtmlFormatter(linenos=numera_righe)
    return highlight(_prepara_testo(testo), _get_lexer(lexer_name), formatter) 
    




class Pyg(object):
    """
    Wrapper per utilizzo del modulo pygments per 'colorare' blocchi di
    codice python. Si ottiene una stringa HTML formattata.
    N.B. il codice css **deve** gia' essere presente a parte
    Adattamento da un codice di esempio dal sito di pygments
    """
    def __init__(self, testo, lexer_name='python'):
        """(list|basestring|object [,str])
        
        Ottiene una oggetto che rappresenta codice da "colorare"
        """
        self._lexer_name = lexer_name
        if isinstance(testo, list) or isinstance(testo, tuple):
            self.testo = "\n".join(testo)
        elif isinstance(testo, basestring):
            self.testo = testo
        else:
            self.testo = str(testo)

    def servizio(self):
        return HtmlFormatter().get_style_defs('.highlight')

    def ottieni_codice_con_numerazione(
        self, numeraRighe='inline',
        wrapStart="<div class='code_console'>\n",
        wrapEnd="</div>\n"  ):
        """
        ([str] [,str] [,str]) -> str
        
        Genera codice corredato dal numero della riga.
        
        Ottiene il pezzo di codice HTML formattato che racchiude il codice
        python 'colorato'.

        Opzionalmente incapsula detto codice in un tag div prescelto
        """
        formatter = HtmlFormatter(
            linenos=numeraRighe, cssclass="code_console"
        )
        return '\n\n%s%s\n\n%s' % (
            wrapStart, highlight(self.testo, self._get_lexer(), formatter), wrapEnd
        )

    def _get_lexer(self):
        try:
            return get_lexer_by_name(self._lexer_name)
        except IndexError as ie:
            raise 'Errore: manca il lexer %s\n%s' % (lexer_name, ie.message)
        
    
    def ottieni_codice(self):
        """([str] [,str] [,str]) -> str
        Ottiene il pezzo di codice HTML formattato che racchiude il codice
        python 'colorato'.
        Opzionalmente incapsula detto codice in un tag div prescelto
        """
        formatter = HtmlFormatter()
        return highlight(self.testo, self._get_lexer(), formatter) 

if __name__ == '__main__':
    testo = []
    testo.append('#!/usr/bin/env python')
    testo.append('class MyObj(object):')
    testo.append('    def __init__(self, num_loops):')
    testo.append('        self.count = num_loops')
    testo.append('def go(self):')
    p = Pyg(testo)
    print p.ottieni_codice()
    



