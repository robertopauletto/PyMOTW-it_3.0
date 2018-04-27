# fetch_podcasts.py

from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser

# Impostazione di qualche variabile globale
num_fetch_threads = 2
enclosure_queue = Queue()

# Una vera applicazione non utilizzerebbe dati
# scritti direttamente nel codice
feed_urls = [
    'http://talkpython.fm/episodes/rss',
]

def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))

def download_enclosures(q):
    """Questa è la funzione di lavoro del thread.
    Elabora gli elementi nella coda uno dopo l'altro.
    Questi thread di demone girano in un ciclo infinito,
    ed escono solamente quando esce il thread principale
    """

    while True:
        message('Cerco la prossima richiesta')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('scaricamento {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        # Salva il file scaricato nella directory corrente
        message('scrittura in {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()

# Impostazione di alcuni thread per ottenere le richieste
for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue,),
        name='worker-{}'.format(i),
    )
    worker.setDaemon(True)
    worker.start()
        
# Scaricamento del/i feed ed inserimento dell'url da scaricare
# nella coda.
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
	for enclosure in entry.get('enclosures', []):
	    parsed_url = urlparse(enclosure['url'])
	    message('accodamento {}'.format(
                parsed_url.path.rpartition('/')[-1]))
            enclosure_queue.put(enclosure['url'])

# Ora si attende lo svuotamento della coda, che indica che abbiamo
# elaborato tutti gli scaricamenti.
message('*** Thread principale in attesa')
enclosure_queue.join()
message('*** fatto')
