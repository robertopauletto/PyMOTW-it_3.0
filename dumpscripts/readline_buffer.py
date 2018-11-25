# readline_buffer.py

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

class BufferAwareCompleter:

    def __init__(self, options):
        self.options = options
        self.current_candidates = []

    def complete(self, text, state):
        response = None
        if state == 0:
            # Questa è la prima volta per questo testo, quindi si costruisce
            # un elenco di corrispondenze

            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            logging.debug('riga originale=%s', repr(origline))
            logging.debug('inizio=%s', begin)
            logging.debug('fine=%s', end)
            logging.debug('in completamento=%s', being_completed)
            logging.debug('parole=%s', words)

            if not words:
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if begin == 0:
                        # prima parola
                        candidates = self.options.keys()
                    else:
                        # parola ulteriore
                        first = words[0]
                        candidates = self.options[first]

                    if being_completed:
                        # cerca corrispondenza di opzioni con la
                        # porzione di input che si sta completando
                        self.current_candidates = [
                            w for w in candidates
                            if w.startswith(being_completed)
                        ]
                    else:
                        # corrispondenza con una stringa vuota,
                        # quindi si usano tutti i candidati
                        self.current_candidates = candidates

                    logging.debug('candidati=%s', self.current_candidates)

                except (KeyError, IndexError) as err:
                    logging.error('errore di completamento: %s', err)
                    self.current_candidates = []

        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logging.debug('completato(%s, %s) => %s', repr(text), state, response)
        return response


def input_loop():
    line = ''
    while line != 'stop':
        line = input('Prompt ("stop" per uscire): ')
        print('Inviato {}'.format(line))


# Registrazione della propria funzione di completamento
readline.set_completer(BufferAwareCompleter(
    {'elenca':['file', 'directory'],
     'stampa':['pernome', 'perdimensione'],
     'stop':[],
    }).complete)


# Uso del tasto tab per il completamento
readline.parse_and_bind('tab: complete')


# Prompt all'utente per il testo
input_loop()
