# multiprocessing_producer_consumer.py

import multiprocessing
import time


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Pilloa avvelenata provoca l'arresto
                print('{}: In uscita'.format(proc_name))
                self.task_queue.task_done()
                break
            print('{}: {}'.format(proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)  # simula il tempo impiegato per eseguire il lavoro
        return '{self.a} * {self.b} = {product}'.format(
            self=self, product=self.a * self.b)

    def __str__(self):
        return '{self.a} * {self.b}'.format(self=self)


if __name__ == '__main__':
    # Costituisce le code di comunicazione
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Partono i consulmatori
    num_consumers = multiprocessing.cpu_count() * 2
    print('Creazione di {} consumatori'.format(num_consumers))
    consumers = [
        Consumer(tasks, results)
        for i in range(num_consumers)
    ]
    for w in consumers:
        w.start()

    # Accodamento lavori
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Aggiunge una pillola avvelenata per ogni consumatore
    for i in range(num_consumers):
        tasks.put(None)

    # Attende la fine di tutti i compiti
    tasks.join()

    # Inizia la stampa dei risultati
    while num_jobs:
        result = results.get()
        print('Resultato:', result)
        num_jobs -= 1
