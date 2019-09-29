# multiprocessing_wordcount.py

import multiprocessing
import string

from multiprocessing_mapreduce import SimpleMapReduce


def file_to_words(filename):
    """Legge un file e ritorna una sequenza di valori
    (parole, occorrenze).
    """
    STOP_WORDS = set([word.strip() for word in open('ita_stopwords.txt')])
    TR = str.maketrans({
        p: ' '
        for p in string.punctuation
    })

    print('{} in lettura {}'.format(
        multiprocessing.current_process().name, filename))
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            # Salta le righe di commento.
            if line.lstrip().startswith(('<', '#', '$')):
                continue
            line = line.translate(TR)  # Elimina la punteggiatura
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append((word, 1))
    return output


def count_words(item):
    """Converte i dati partizionati per una parola in una tupla
    che contiene la parola e il numero di occorrenze
    .
    """
    word, occurences = item
    return (word, sum(occurences))


if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('../tran/multiprocessing.xml')

    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    print('\nLE 20 PAROLE PIU\' FREQUENTI\n')
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print('{word:<{len}}: {count:5}'.format(
            len=longest + 1,
            word=word,
            count=count)
        )
