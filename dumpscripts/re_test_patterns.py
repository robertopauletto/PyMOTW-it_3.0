# re_test_patterns.py

import re


def test_patterns(text, patterns=[]):
    """Dato un testo sorgente ed un elenco di modelli, cerca
    corrispondenze per ogni modello all'interno del testo e le
    stampa a stdout
    """
    # Cerca ogni modello nel testo e stampa il risultato
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return

if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa',
                  [('ab', "'a' seguito da 'b'"),
                   ])
