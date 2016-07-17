#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Moduli di sistem
from Queue import Queue
from threading import Thread
import time

# Mouli locali
import feedparser

# Impostazione di alcune variabili locali
num_fetch_threads = 2
enclosure_queue = Queue()

# Una vera applicazione non utilizzerebbe dati hard-coded ...
#feed_urls = [ 'http://www.castsampler.com/cast/feed/rss/guest',
             #]

# Il feed di esempio originale è stato commentato in quanto esso non esiste
# più; al suo posto si utilizza il feed rss del sito PyMotw-it
feed_urls = [ 'http://robyp.x10host.com/pymotw-it_feed.xml',
              ]


def downloadEnclosures(i, q):
    """Questa è la funzione di lavoro del thread.
    Elabora gli elementi nella coda uno dopo l'altro.
    Questi deamon thread girano in un loop infinito,
    ed escono solamente quando esce il thread principale
    """
    while True:
        print '%s: Cerco la prossima richiesta' % i
        url = q.get()
        print '%s: Scaricamento:' % i, url
        # invece di scaricare veramente l'URL
        # si fa finta e si mette in pausa il programma
        time.sleep(i + 2)
        q.task_done()


# Impostazione di alcuni thread per ottenere le richieste
for i in range(num_fetch_threads):
    worker = Thread(target=downloadEnclosures, args=(i, enclosure_queue,))
    worker.setDaemon(True)
    worker.start()

# Scaricamento del/i feed ed inserimento dell'url da scaricare
# nella coda.

# Il ciclo seguente è stato modificato dal traduttore in quanto il
# feed di esempio originale non è più disponibile
# -------------- INIZIO CODICE MODIFICATO --------------------------
for url in feed_urls:
    response = feedparser.parse(url)
    for i, entry in enumerate(response['entries']):
        print 'Accodamento:', entry.link
        enclosure_queue.put(entry.link)
        if i == 9:  # Per semplicità prendo solo 10 elementi
            break
# -------------- FINE CODICE MODIFICATO ----------------------------



# Ora si attende lo svuotamento della coda, che indica che abbiamo 
# elaborato tutti gli scaricamenti.
print '*** Thread principale in attesa'
enclosure_queue.join()
print '*** Fatto'