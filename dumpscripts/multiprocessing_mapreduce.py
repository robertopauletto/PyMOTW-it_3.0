# multiprocessing_mapreduce.py

import collections
import itertools
import multiprocessing


class SimpleMapReduce:

    def __init__(self, map_func, reduce_func, num_workers=None):
        """
        map_func

          Funzione che mappa gli input a dati intermedi. Riceve
          come argomento un valore in input e ritorna un tupla
          con la chiave ed il valore che devono essere ridotti.

        reduce_func

          Funzione per ridurre la versione partizionata di dati
          intermedi verso il risultato finale. Riceve come
          argomento una chiave prodotta da map_func e una sequenza
          dei valori associati a quella chiave

        num_workers

          Il numero di esecutiori da creare nel pool. Il valore
          predefinito è il numero di CPU disponibili nell'host
          corrente.
        """
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        """Sistema i valori mappati in base alle loro chiavi.
        Ritorna una sequanza non ordinata di tuple con una chiave
        e una sequenza di valori
        """
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        """Elabora l'input tramite le funzioni di mae e reduce
        passate.

        inputs
          Un iterabile che contiene i dati ininput da elaborare

        chunksize=1
          La porzione di dati in put da passare a ciascun esecutore
          Può essere usato per sintonizzare le prestazioni durante
          la fase di mappatura.
        """
        map_responses = self.pool.map(
            self.map_func,
            inputs,
            chunksize=chunksize,
        )
        partitioned_data = self.partition(
            itertools.chain(*map_responses)
        )
        reduced_values = self.pool.map(
            self.reduce_func,
            partitioned_data,
        )
        return reduced_values
