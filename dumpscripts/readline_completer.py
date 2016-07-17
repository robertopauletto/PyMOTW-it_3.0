#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import readline
import logging

LOG_FILENAME = '/tmp/completer.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )

class SimpleCompleter(object):
    
    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # Questa è la prima volta per questo testo, quindi si costruisce un elenco di corrispondenze
            if text:
                self.matches = [s 
                                for s in self.options
                                if s and s.startswith(text)]
                logging.debug('%s corrisponde a: %s', repr(text), self.matches)
            else:
                self.matches = self.options[:]
                logging.debug('(input vuoto) corrisponde a: %s', self.matches)
        
        # Restituisce l'elemento che corrisponde a state dalla lista di completamento
        # se ce ne sono a sufficienza
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug('completato(%s, %s) => %s', 
                      repr(text), state, repr(response))
        return response

def input_loop():
    line = ''
    while line != 'stop':
        line = raw_input('Prompt ("stop" per uscire): ')
        print 'Inviato %s' % line

# Registra la funzione di completamento
readline.set_completer(SimpleCompleter(['start', 'stop', 'list', 'print']).complete)

# Usa il tasto tab per il completamento
readline.parse_and_bind('tab: complete')

# Prompt all'utente per il testo
input_loop()