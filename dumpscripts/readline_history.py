# readline_history.py

try:
    import gnureadline as readline
except ImportError:
    import readline
import logging
import os

LOG_FILENAME = '/tmp/completer.log'
HISTORY_FILENAME = '/tmp/completer.hist'

logging.basicConfig(
    format='%(message)s',
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)


def get_history_items():
    num_items = readline.get_current_history_length() + 1
    return [
        readline.get_history_item(i)
        for i in range(1, num_items)
    ]


class HistoryCompleter:

    def __init__(self):
        self.matches = []
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            history_values = get_history_items()
            logging.debug('storico: %s', history_values)
            if text:
                self.matches = sorted(
                    h
                    for h in history_values
                    if h and h.startswith(text)
                )
            else:
                self.matches = []
            logging.debug('corrispondenze: %s', self.matches)
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug('completato(%s, %s) => %s',
                      repr(text), state, repr(response))
        return response


def input_loop():
    if os.path.exists(HISTORY_FILENAME):
        readline.read_history_file(HISTORY_FILENAME)
    print('Lunghezza max file storico:',
          readline.get_history_length())
    print('Storico di partenza:', get_history_items())
    try:
        while True:
            line = input('Prompt ("stop" per uscire): ')
            if line == 'stop':
                break
            if line:
                print('Aggiunta di {!r} allo storico'.format(line))
    finally:
        print('Storico finale:', get_history_items())
        readline.write_history_file(HISTORY_FILENAME)


# Registra la funzione di completamento
readline.set_completer(HistoryCompleter().complete)


# Uso del tasto tab per il completamento
readline.parse_and_bind('tab: complete')


# Prompt all'utente per il testo
input_loop()
