# readline_completer.py


try:
    import gnureadline as readline
except ImportError:
    import readline
import logging

LOG_FILENAME = '/tmp/completer.log'
logging.basicConfig(
    format='%(message)s',
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)


class SimpleCompleter:

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        response = None
        if state == 0:
            # Questa è la prima volta per questo testo, quindi si
            # costruisce un elenco di corrispondenze
            if text:
                self.matches = [
                    s
                    for s in self.options
                    if s and s.startswith(text)
                ]
                logging.debug('%s corrispondenze: %s',
                              repr(text), self.matches)
            else:
                self.matches = self.options[:]
                logging.debug('(input vuoto) corrispondenze: %s',
                              self.matches)

        # Restituisce l'elemento che corrisponde a state dalla
        # lista di completamento se ce ne sono a sufficienza
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
        line = input('Prompt ("stop" per abbandonare): ')
        print('Invia {}'.format(line))


# Registra la funzione di completamento
OPTIONS = ['start', 'stop', 'elenco', 'stampa']
readline.set_completer(SimpleCompleter(OPTIONS).complete)

# Usa il tasto tab per il completamento
readline.parse_and_bind('tab: complete')

# Richiede testo all'utente
input_loop()
